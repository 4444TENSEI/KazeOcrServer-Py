from config.loader import init_config


# 初始化配置
env_config = init_config()

# 配置读取
ENV_DEBUG = env_config.get("debug")
ENV_PORT = env_config.get("port")
ENV_API_KEY = env_config.get("api_key")


print(f"配置载入成功: {env_config}")
