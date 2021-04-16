import os

from app import create_app, db
from app.model import User, Role

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

@app.route("/")
def index():
    return jsonify({'msg': 'Main page'})

@app.route("/message")
def message():
    return jsonify({"message": "hola mundo 😎"})
