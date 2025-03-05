#pylint:disable=W0718,W0611

# Swagger Docs
from src.main.docs.swagger_blueprint import send_file

from src.main.server.server import Server

if __name__ == "__main__":
    app = Server.create_app()