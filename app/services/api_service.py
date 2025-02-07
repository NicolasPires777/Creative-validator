import requests
import os

class ApiService:
    def __init__(self):
        self.api_url = os.getenv('BACKSTAGE_API_URL', 'http://backstage.apis.zedia.com.br/api/v1/orders/order')

    def get_order_lines(self, order_id):
        try:
            url = f"{self.api_url}/{order_id}"
            response = requests.get(url)
            response.raise_for_status()  # Lança uma exceção para respostas não bem-sucedidas

            order_data = response.json()
            lines = [line['name'] for line in order_data.get('lines', [])]
            return lines
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro ao acessar a API: {e}")
        except Exception as e:
            raise Exception(f"Erro ao processar os dados da API: {e}")