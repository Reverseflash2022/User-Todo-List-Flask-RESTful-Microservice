from flask import request, jsonify, current_app as app
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from . import services
from .errors import ValidationError

def init_app(app):
    @app.route('/api/v1/register', methods=['POST'])
    def register():
        username = request.json.get('username')
        password = request.json.get('password')
        if not username or not password:
            raise ValidationError('Username and password required')
        user = services.create_user(username, password)
        return jsonify(id=user.id, username=user.username), 201

    @app.route('/api/v1/login', methods=['POST'])
    def login():
        username = request.json.get('username')
        password = request.json.get('password')
        if not username or not password:
            raise ValidationError('Username and password required')
        user = services.authenticate_user(username, password)
        if not user:
            return jsonify(message="Invalid username or password"), 401
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200

    @app.route('/api/v1/todos', methods=['POST'])
    @jwt_required()
    def create_todo():
        user_id = get_jwt_identity()
        title = request.json.get('title')
        description = request.json.get('description')
        if not title:
            raise ValidationError('Title is required')
        todo = services.create_todo(user_id, title, description)
        return jsonify(id=todo.id, title=todo.title, description=todo.description, completed=todo.completed), 201

    @app.route('/api/v1/todos', methods=['GET'])
    @jwt_required()
    def get_todos():
        user_id = get_jwt_identity()
        todos = services.get_todos(user_id)
        return jsonify([todo.to_dict() for todo in todos]), 200

    @app.route('/api/v1/todos/<int:todo_id>', methods=['PUT'])
    @jwt_required()
    def update_todo(todo_id):
        user_id = get_jwt_identity()
        title = request.json.get('title')
        description = request.json.get('description')
        completed = request.json.get('completed')
        todo = services.update_todo(user_id, todo_id, title, description, completed)
        return jsonify(todo.to_dict()), 200

    @app.route('/api/v1/todos/<int:todo_id>', methods=['DELETE'])
    @jwt_required()
    def delete_todo(todo_id):
        user_id = get_jwt_identity()
        services.delete_todo(user_id, todo_id)
        return '', 204

