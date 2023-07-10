# BaseBot

基于 MVC 模型的基础 HttpApi 机器人框架，可以快速开发相关机器人。

请在 `.env` 文件中配置相关参数。

## 目录结构

```markdown
.
├── app # 业务逻辑
│ ├── controller.py
│ ├── event.py
│ ├── __pycache__
│ └── setting.py
├── cache # 缓存
│ ├── base.py
│ ├── elara.py
│ ├── __init__.py
│ └── redis.py
├── main.py # 主程序
├── requirements.txt
├── run.log # 运行日志
├── schema.py # 数据模型
└── utils # 工具
└── parse.py
```

## 缓存

缓存使用 `redis`，请在 `.env` 文件中配置相关参数。
直接实例化即可使用。

redis 会在程序启动时自动连接，初始化一个 cache 对象。