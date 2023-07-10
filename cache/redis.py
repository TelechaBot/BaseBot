# -*- coding: utf-8 -*-
# @Time    : 2023/7/10 下午9:43
# @Author  : sudoskys
# @File    : redis.py
# @Software: PyCharm
import json
import os

import redis
from dotenv import load_dotenv
from loguru import logger
from redis.asyncio.client import Redis
from redis.asyncio.connection import ConnectionPool

from cache.base import AbstractDataClass, PREFIX


class RedisClientWrapper(AbstractDataClass):
    """
    Redis 数据类
    """

    def __init__(self, backend, prefix=PREFIX):
        self.prefix = prefix
        self.connection_pool = redis.asyncio.ConnectionPool.from_url(backend)
        self._redis = redis.asyncio.Redis(connection_pool=self.connection_pool)

    async def ping(self):
        return await self._redis.ping()

    def update_backend(self, backend):
        self.connection_pool = ConnectionPool.from_url(backend)
        self._redis = Redis(connection_pool=self.connection_pool)
        return True

    async def set_data(self, key, value, timeout=None):
        if isinstance(value, (dict, list)):
            value = json.dumps(value)
        return await self._redis.set(name=f"{self.prefix}{key}", value=value, ex=timeout)

    async def read_data(self, key):
        data = await self._redis.get(self.prefix + str(key))
        if data is not None:
            try:
                data = json.loads(data)
            except Exception as e:
                pass
        return data


def check_redis_dsn(dsn):
    try:
        r = redis.Redis.from_url(dsn)
        assert r.ping() is True
    except Exception as exp:
        print("Error connecting to Redis: ", exp)
        return False
    else:
        return True


# 加载 .env 文件
load_dotenv()
redis_url = os.getenv('REDIS_DSN', 'redis://localhost:6379/0')
try:
    # 检查连接
    if not check_redis_dsn(redis_url):
        raise ValueError('REDIS DISCONNECT')
        # 初始化实例
    cache: RedisClientWrapper = RedisClientWrapper(redis_url)
except Exception as e:
    logger.error(e)
    if redis_url == 'redis://localhost:6379/0':
        logger.error('REDIS DISCONNECT:Ensure Configure the REDIS_DSN variable in .env')
    raise ValueError('REDIS DISCONNECT')
else:
    logger.success(f'RedisClientWrapper loaded successfully in {redis_url}')
