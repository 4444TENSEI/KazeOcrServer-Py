from flask import Blueprint, redirect

# 静态资源目录
bp_web = Blueprint("bp_web", __name__, url_prefix="/doc")


# 首页
@bp_web.route("")
def doc_page():
    return redirect("https://s.apifox.cn/cac0897a-370e-407c-ba9e-de27c905ff1f", 302)
