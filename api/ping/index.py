import datetime, socket
from flask import Blueprint, jsonify, request


# 蓝图
bp_ping = Blueprint("bp_ping", __name__, url_prefix="/api/ping")


@bp_ping.route("", methods=["GET"])
def ping():
    # 核心响应信息
    response = {
        "headers": dict(request.headers),
        "hostname": socket.gethostname(),
        # 获取客户端真实IP（处理代理服务器情况）
        "ip": {
            "real": request.headers.getlist("X-Real-IP"),
            "forwarded": request.headers.getlist("X-Forwarded-For"),
            "remote": request.remote_addr,
        },
        "time": datetime.datetime.utcnow().isoformat() + "Z",
    }
    return jsonify(response), 200
