import json, os

config_path = "./config.json"
config_sys_name = "FLASK_IP_CONFIG"


def _load_config_from_source(source_type, source, error_prefix):
    """统一配置加载逻辑（环境变量/文件）"""
    try:
        if source_type == "env":
            raw_data = source
        else:  # 文件类型
            with open(source, "r", encoding="utf-8") as f:
                raw_data = f.read()
        return json.loads(raw_data)
    except json.JSONDecodeError as e:
        raise ValueError(f"{error_prefix}内容非标准JSON格式：{e}")
    except FileNotFoundError:
        raise ValueError(f"{error_prefix}未找到，请检查路径是否存在")


def init_config():
    # 优先级1: 环境变量
    env_config = os.getenv(config_sys_name)
    if env_config:
        print(f"尝试载入环境变量配置: {config_sys_name}")
        return _load_config_from_source(
            source_type="env",
            source=env_config,
            error_prefix=f"环境变量 '{config_sys_name}'",
        )
    # 优先级2: 本地文件
    print(f"未找到环境变量 '{config_sys_name}'，尝试载入文件: {config_path}")
    return _load_config_from_source(
        source_type="file", source=config_path, error_prefix=f"配置文件 '{config_path}'"
    )
