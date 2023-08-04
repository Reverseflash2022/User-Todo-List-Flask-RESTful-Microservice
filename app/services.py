from werkzeug.exceptions import NotFound
from . import db
from .models import User, Todo

def create_user(username, password):
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return None

def create_todo(user_id, title, description=None):
    todo = Todo(user_id=user_id, title=title, description=description)
    db.session.add(todo)
    db.session.commit()
    return todo

def get_todos(user_id):
    return Todo.query.filter_by(user_id=user_id).all()

def get_todo(user_id, todo_id):
    todo = Todo.query.filter_by(user_id=user_id, id=todo_id).first()
    if not todo:
        raise NotFound('Todo not found')
    return todo

def update_todo(user_id, todo_id, title=None, description=None, completed=None):
    todo = get_todo(user_id, todo_id)
    if title is not None:
        todo.title = title
    if description is not None:
        todo.description = description
    if completed is not None:
        todo.completed = completed
    db.session.commit()
    return todo

def delete_todo(user_id, todo_id):
    todo = get_todo(user_id, todo_id)
    db.session.delete(todo)
    db.session.commit()
