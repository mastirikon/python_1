from math import log
import os

from flask import Blueprint, jsonify, request, send_from_directory
from werkzeug.utils import secure_filename

files_bp = Blueprint("files", __name__)


@files_bp.route('/health', methods=["GET"])
def health():
    
    print("request", request.blueprint)
    
    return jsonify({
        "status": "ok",
        "service": "file_transfer"
    }), 200


# Загрузка файла на сервер
@files_bp.route('/upload', methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "file field required"}), 400
    
    file = request.files["file"]
    print("file", file)
    
    if file.filename == "":
        return jsonify({"error": "empty filename"}), 400
    
    filename = secure_filename(str(file.filename))
    print('filename: ', filename)
    
    filepath = os.path.join(os.getcwd(), "src", "upload", filename)
    print("filepath: ", filepath)
    
    file.save(filepath)

    return (jsonify({ 
        "message": "uploaded", 
        "filename": filename 
    }), 201)


@files_bp.route('/download/<filename>', methods=["GET"])
def download_file(filename):
    print('filename: ', filename)
    
    upload_folder = os.path.join(os.getcwd(), "src", "upload")
    print('upload_folder: ', upload_folder)
    
    filepath = os.path.join(upload_folder, filename)
    print('filepath: ', filepath)
    
    if not os.path.exists(filepath):
        return (jsonify({"error": "file not found"}), 404)
    
    return send_from_directory(upload_folder, filename, as_attachment=True)