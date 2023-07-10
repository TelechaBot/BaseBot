# 🧀 BaseBot

基于 MVC 模型的基础 HttpApi 机器人框架，可以快速开发相关机器人。

请在 `.env` 文件中配置相关参数。

## 目录结构

```markdown
.
├── app # 业务逻辑
│ ├── controller.py # 控制器
│ ├── event.py # 事件处理
│ ├── __pycache__
│ └── setting.py # 业务配置模型，可以在此处配置相关参数并在 .env 文件中读取初始化。
├── cache # 缓存
│ ├── base.py
│ ├── elara.py # 文件缓存模型
│ ├── __init__.py
│ └── redis.py # redis 缓存模型
├── main.py # 主程序
├── requirements.txt
├── run.log # 运行日志
├── schema.py # 数据模型
└── utils # 工具
└── parse.py # 解析器
```

## 缓存

缓存使用 `redis`，请在 `.env` 文件中配置相关参数。
直接实例化即可使用。

redis 会在程序启动时自动连接，初始化一个 cache 对象。
