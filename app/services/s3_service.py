import os
import boto3
from botocore.exceptions import ClientError
from PIL import Image
import re
import shutil

class S3Service:
    def __init__(self):
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=os.getenv('AWS_REGION')
        )
        self.bucket_name = os.getenv('S3_BUCKET_NAME')
        self.base_path = os.getenv('S3_BASE_PATH')
        self.downloads_folder = 'downloads'  # Pasta onde os arquivos serão salvos

        # Cria a pasta 'downloads' se nao existir
        os.makedirs(self.downloads_folder, exist_ok=True)

    def download_folder(self, folder_name):
        try:
            # Cria o caminho completo para a pasta local
            local_path = os.path.join(self.downloads_folder, folder_name)
            os.makedirs(local_path, exist_ok=True)

            # Define o prefixo para a pasta 'assets' dentro do diretório fornecido
            s3_prefix = f"{self.base_path}{folder_name}/assets/"

            print(f"Procurando no S3 com prefixo: {s3_prefix}")  # Log para depuração

            # Lista e baixa os arquivos do S3
            paginator = self.s3.get_paginator('list_objects_v2')
            page_iterator = paginator.paginate(
                Bucket=self.bucket_name,
                Prefix=s3_prefix
            )

            for page in page_iterator:
                if 'Contents' not in page:
                    print("Nenhum arquivo encontrado no prefixo especificado.")  # Log para depuração
                    break

                for obj in page.get('Contents', []):
                    file_key = obj['Key']
                    # Remove o prefixo do S3 para criar o caminho local relativo
                    relative_path = os.path.relpath(file_key, s3_prefix)
                    local_file_path = os.path.join(local_path, relative_path)
                    os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
                    self.s3.download_file(self.bucket_name, file_key, local_file_path)
                    print(f"Downloaded: {file_key} -> {local_file_path}")  # Log para depuração

            return local_path
        except ClientError as e:
            raise Exception(f"S3 Error: {e}")
        except Exception as e:
            raise Exception(f"Download Failed: {e}")
        
    def validate_images(self, folder_name, lines):
        validation_results = []
        for line in lines:
            if line.endswith("squeeze"):
                bottom_image_path = os.path.join(self.downloads_folder, folder_name, f"{line}_bottom.png")
                bottom_status = self._check_image(bottom_image_path, (1024, 144))
                validation_results.append(f"{line}_bottom: {bottom_status}")            
                side_image_path = os.path.join(self.downloads_folder, folder_name, f"{line}_side.png")
                side_status = self._check_image(side_image_path, (256, 720))
                validation_results.append(f"{line}_side: {side_status}")
                adjusted_line = re.sub(r"_squeeze$", "", line)
                maxpage_image_path = os.path.join(self.downloads_folder, folder_name, f"{adjusted_line}_maxpage.png")
                maxpage_status = self._check_image(maxpage_image_path, (1280, 720))
                validation_results.append(f"{adjusted_line}_maxpage: {maxpage_status}")
            elif line.endswith("squeezee"):
                bottom_image_path = os.path.join(self.downloads_folder, folder_name, f"{line}_bottom.png")
                bottom_status = self._check_image(bottom_image_path, (1024, 720))
                validation_results.append(f"{line}_bottom: {bottom_status}")
                side_image_path = os.path.join(self.downloads_folder, folder_name, f"{line}_side.png")
                side_status = self._check_image(side_image_path, (256, 720))
                validation_results.append(f"{line}_side: {side_status}")
                adjusted_line = re.sub(r"_squeezee$", "", line)
                maxpage_image_path = os.path.join(self.downloads_folder, folder_name, f"{adjusted_line}_maxpage.png")
                maxpage_status = self._check_image(maxpage_image_path, (1280, 720))
                validation_results.append(f"{adjusted_line}_maxpage: {maxpage_status}")
            elif line.endswith("float"):
                bottom_image_path = os.path.join(self.downloads_folder, folder_name, f"{line}_1.png")
                bottom_status = self._check_image(bottom_image_path, (1280, 105))
                validation_results.append(f"{line}_1: {bottom_status}")               
                side_image_path = os.path.join(self.downloads_folder, folder_name, f"{line}_2.png")
                side_status = self._check_image(side_image_path, (1280, 105))
                validation_results.append(f"{line}_2: {side_status}")
                adjusted_line = re.sub(r"_float$", "", line)
                maxpage_image_path = os.path.join(self.downloads_folder, folder_name, f"{adjusted_line}_maxpage.png")
                maxpage_status = self._check_image(maxpage_image_path, (1280, 720))
                validation_results.append(f"{adjusted_line}_maxpage: {maxpage_status}")
            elif line.endswith("skcf"):
                bottom_image_path = os.path.join(self.downloads_folder, folder_name, f"{line}_1.png")
                bottom_status = self._check_image(bottom_image_path, (220, 720))
                validation_results.append(f"{line}_1: {bottom_status}")
                side_image_path = os.path.join(self.downloads_folder, folder_name, f"{line}_2.png")
                side_status = self._check_image(side_image_path, (220, 720))
                validation_results.append(f"{line}_2: {side_status}")
                adjusted_line = re.sub(r"_skcf$", "", line)
                maxpage_image_path = os.path.join(self.downloads_folder, folder_name, f"{adjusted_line}_maxpage.png")
                maxpage_status = self._check_image(maxpage_image_path, (1280, 720))
                validation_results.append(f"{adjusted_line}_maxpage: {maxpage_status}")
            elif line.endswith("skch"):
                skch1_image_path = os.path.join(self.downloads_folder, folder_name, f"{line}_1.png")
                skch1_status = self._check_image(skch1_image_path, (220, 540))
                validation_results.append(f"{line}_1: {skch1_status}")
                skch2_image_path = os.path.join(self.downloads_folder, folder_name, f"{line}_2.png")
                skch2_status = self._check_image(skch2_image_path, (220, 540))
                validation_results.append(f"{line}_2: {skch2_status}")
                adjusted_line = re.sub(r"_skch$", "", line)
                maxpage_image_path = os.path.join(self.downloads_folder, folder_name, f"{adjusted_line}_maxpage.png")
                maxpage_status = self._check_image(maxpage_image_path, (1280, 720))
                validation_results.append(f"{adjusted_line}_maxpage: {maxpage_status}")
            elif line.endswith("opening"):
                opening_image_path = os.path.join(self.downloads_folder, folder_name, f"{line}.png")
                opening_status = self._check_image(opening_image_path, (626, 124))
                validation_results.append(f"{line}: {opening_status}")
                adjusted_line = re.sub(r"_opening$", "", line)
                maxpage_image_path = os.path.join(self.downloads_folder, folder_name, f"{adjusted_line}_maxpage.png")
                maxpage_status = self._check_image(maxpage_image_path, (1280, 720))
                validation_results.append(f"{adjusted_line}_maxpage: {maxpage_status}")

        return validation_results

    def _check_image(self, image_path, expected_resolution):
        if not os.path.exists(image_path):
            return "nao encontrado"

        try:
            with Image.open(image_path) as img:
                width, height = img.size
                if (width, height) == expected_resolution:
                    return "verificado"
                else:
                    return f"na resolucao errada ({width}x{height})"
        except Exception as e:
            return f"erro ao verificar: {str(e)}"
        
    @staticmethod
    def excluir_pasta_downloads():
        # Obtém o caminho absoluto da raiz do projeto
        raiz_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
        # Caminho da pasta Downloads na raiz do projeto
        caminho_downloads = os.path.join(raiz_projeto, "Downloads")
        if os.path.exists(caminho_downloads):
            shutil.rmtree(caminho_downloads)  # Remove a pasta e todo o conteúdo
            print("Pasta 'Downloads' excluída com sucesso.")
        else:
            print("A pasta 'Downloads' nao existe.")