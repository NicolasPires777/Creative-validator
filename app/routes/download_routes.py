from flask import Blueprint
from app.controllers.download_controller import DownloadController

download_bp = Blueprint('verify', __name__)

@download_bp.route('/verify/<string:folder_name>', methods=['GET'])
def download_folder(folder_name):
    return DownloadController.download_folder(folder_name)