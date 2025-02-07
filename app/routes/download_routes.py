from flask import Blueprint
from app.controllers.download_controller import DownloadController

download_bp = Blueprint('download', __name__)

@download_bp.route('/download/<string:folder_name>', methods=['GET'])
def download_folder(folder_name):
    return DownloadController.download_folder(folder_name)