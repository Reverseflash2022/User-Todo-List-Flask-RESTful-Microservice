import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, g, json, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_limiter.util import get_remote_address
from flask_limiter import Limiter
from werkzeug.exceptions import HTTPException
from config import get_config
from app.errors import ValidationError

# Initialize extensions outside of the create_app function
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()
limiter = Limiter(key_func=get_remote_address, default_limits=["5 per minute"])

def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())

    # Initialize extensions with the app inside the create_app function
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)  # Initialize Flask-Migrate after the db
    limiter.init_app(app)

    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/todo-microservice.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Todo microservice startup')

    # Error handling
    @app.errorhandler(HTTPException)
    def handle_http_error(e):
        response = e.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response

    @app.errorhandler(ValidationError)
    def handle_validation_error(e):
        return jsonify(error=e.message), 400

    from . import models, routes, services
    routes.init_app(app)

    return app
