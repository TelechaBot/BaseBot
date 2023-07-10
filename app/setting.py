# -*- coding: utf-8 -*-
# @Time    : 2023/7/10 下午9:28
# @Author  : sudoskys
# @File    : setting.py
# @Software: PyCharm
from dotenv import load_dotenv
from pydantic import BaseSettings, Field


class BotSetting(BaseSettings):
    """
    代理设置
    """
    link: str = Field(None, env='BOT_LINK')
    token: str = Field(None, env='BOT_TOKEN')
    proxy_address: str = Field(None, env="BOT_PROXY_ADDRESS")  # "all://127.0.0.1:7890"

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


load_dotenv()
BotSetting = BotSetting()
