import os
from flask import send_file
from flask_swagger_ui import get_swaggerui_blueprint
from src.main.server.server import Server

SWAGGER_URL = "/api/docs"
API_URL = "/swagger.yaml"

swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
Server.app.register_blueprint(swagger_ui_blueprint)

SWAGGER_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "swagger.yaml")

@Server.app.route("/swagger.yaml")
def swagger_file():
    if not os.path.exists(SWAGGER_FILE_PATH):
        print("Erro: swagger.yaml não encontrado no caminho:", SWAGGER_FILE_PATH)
        return "Arquivo swagger.yaml não encontrado", 404
    return send_file(SWAGGER_FILE_PATH)
