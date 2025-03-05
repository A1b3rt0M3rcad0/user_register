from flask import Flask
from src.main.routes.routes import user_routes_bp

class Server:

    app = Flask(__name__)
    app.register_blueprint(user_routes_bp)
    
    @classmethod
    def run(cls, **kwargs) -> None:
        cls.app.run(**kwargs)