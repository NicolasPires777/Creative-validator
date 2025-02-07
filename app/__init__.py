from flask import Flask
from app.routes.download_routes import download_bp
import os
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)
    
    load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env
    
    # Registrar Blueprints
    app.register_blueprint(download_bp, url_prefix='/api')
    
    return app