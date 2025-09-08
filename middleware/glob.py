from flask import request, jsonify

# 配置
from config.init import ENV_API_KEY

# 定义白名单路由（无需token验证）
PUBLIC_API = ["/", "/doc"]


def midd_glob(app):
    # 捕捉404错误
    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify({"code": 404, "message": "你来到了一个不存在的地方"}), 404

    # 捕捉500错误
    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({"code": 500, "message": "服务器炸了"}), 500

    # 请求拦截
    @app.before_request
    def token_check_middleware():
        # 检查是否在白名单中
        if request.path in PUBLIC_API:
            return None  # 放行
        # 检查URL参数中是否存在token
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"code": 401, "message": "未授权访问"}), 401
        if token != ENV_API_KEY:
            return jsonify({"code": 403, "message": "权限不足"}), 403
