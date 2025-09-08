from flask import Blueprint, jsonify, request
from io import BytesIO
import ddddocr

bp_ocr = Blueprint("bp_ocr", __name__, url_prefix="/api/ocr")
# 初始化ddddocr
ocr = ddddocr.DdddOcr(show_ad=False)

# 允许的文件扩展名
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "bmp", "gif", "webp"}

# 文件大小合规，单位MB
ALLOWED_SIZE = 2


# 图像ocr接口
@bp_ocr.route("/img", methods=["POST"])
def ocr_img():
    img_file = request.files.get("img")
    if not img_file:
        return jsonify(
            {
                "code": 400,
                "message": "必须上传图片文件!",
            }
        )
    # 3. 检查文件扩展名
    if not allowed_file(img_file.filename):
        return jsonify(
            {
                "code": 400,
                "message": "不支持的文件类型!仅支持: " + ", ".join(ALLOWED_EXTENSIONS),
            }
        )
    # 4. 检查文件大小
    if not check_file_size(img_file, ALLOWED_SIZE):
        return jsonify(
            {
                "code": 400,
                "message": "文件大小不能超过 " + str(ALLOWED_SIZE) + "MB!",
            }
        )
    img_file = BytesIO(img_file.read())
    result = ocr.classification(img_file.getvalue())
    if not result:
        return "未识别到内容"
    return result


# 检查文件类型合规
def allowed_file(filename) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    if not allowed_file(img_file.filename):
        return False
    return True


# 检查文件大小合规，单位MB
def check_file_size(file, size):
    # 4. (可选但推荐) 检查文件大小
    # 获取文件大小 (字节)
    file_size = len(file.read())
    file.seek(0)  # 将文件指针重置回开头，因为后面还要读取
    MAX_SIZE = size * 1024 * 1024  # MB
    if file_size > MAX_SIZE:
        return False
    return True
