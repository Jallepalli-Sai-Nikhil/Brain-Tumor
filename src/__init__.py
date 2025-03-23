from flask import Flask
from src.routes.main_bp import main_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    return app