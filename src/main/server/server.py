from flask import Flask
from src.main.routes.routes import user_routes_bp

class Server:

    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.app.register_blueprint(user_routes_bp)
    
    def run(self, **kwargs) -> None:
        self.app.run(**kwargs)