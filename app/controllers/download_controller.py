from flask import jsonify
from app.services.s3_service import S3Service
from app.services.api_service import ApiService

class DownloadController:
    @staticmethod
    def download_folder(order_id):
        try:
            # Baixar as imagens do S3
            s3_service = S3Service()
            download_path = s3_service.download_folder(order_id)

            # Coletar os nomes das lines da campanha
            api_service = ApiService()
            lines = api_service.get_order_lines(order_id)

            # Validar as imagens baixadas
            validation_results = s3_service.validate_images(order_id, lines)

            # Exclui a pasta downloads
            s3_service.excluir_pasta_downloads()

            return jsonify({
                'status': 'success',
                'message': f'Folder {order_id} downloaded successfully',
                'lines': lines,
                'validation_results': validation_results,
                'download_path': download_path
            }), 200
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': str(e)
            }), 500