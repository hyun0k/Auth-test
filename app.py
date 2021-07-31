from flask import Flask

from view import create_endpoints

def create_app():
    app = Flask(__name__)

    create_endpoints(app)
    
    return app