from flask import Flask
from flask_cors import CORS

# 配置
from config.init import ENV_DEBUG, ENV_PORT

# 中间件
from middleware.glob import midd_glob

# 接口
from api.ping.index import bp_ping
from api.doc.index import bp_web
from api.ocr.index import bp_ocr


def create_app():
    app = Flask(__name__)
    # 跨域
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    # 禁用响应结果json转义
    app.json.ensure_ascii = False
    # 中间件
    midd_glob(app)

    # 蓝图注册
    app.register_blueprint(bp_ocr)
    app.register_blueprint(bp_ping)
    app.register_blueprint(bp_web)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=ENV_DEBUG, port=ENV_PORT)
