#pylint:disable=W0718,W0611
from src.main.server.server import Server

# Swagger Docs
from src.main.docs.swagger_blueprint import send_file

if __name__ == "__main__":
    Server.run(host="0.0.0.0", port=5000, debug=True)