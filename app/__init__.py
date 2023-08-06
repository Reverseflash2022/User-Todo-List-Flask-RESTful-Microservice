from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from config import get_config

# Initialize extensions outside of the create_app function
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())

    # Initialize extensions with the app inside the create_app function
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)  # Initialize Flask-Migrate after the db

    from . import models, routes, services
    routes.init_app(app)
    return app

