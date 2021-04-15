from flask import jsonify

from . import main

@main.route('/message')
def index():
    return jsonify({'message': 'Hola Mundo'})
