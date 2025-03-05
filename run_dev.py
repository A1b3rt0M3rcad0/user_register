#pylint:disable=W0718,W0611

# Swagger Docs
from src.main.docs.swagger_blueprint import send_file

from src.main.server.server import Server
from dotenv import load_dotenv
import os


if __name__ == "__main__":
    load_dotenv()
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
    Server.run(host=HOST, port=int(PORT), debug=True)