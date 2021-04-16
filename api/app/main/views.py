from flask import jsonify, request

from . import main
from .. import db
from ..model import Post


@main.route('/posts', methods=['GET'])
def posts():
    posts = Post.query.filter_by(active=True).all()
    if posts:
        return jsonify({'posts': [p.to_json() for p in posts]}), 200
    return jsonify({'msg': 'There are no posts'}), 404


@main.route('/posts', methods=['POST'])
def new_post():
    post = Post.from_json(request.json)
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_json()), 201


@main.route('/posts/<int:id>')
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.to_json())


@main.route('/posts/<int:id>', methods=['PUT'])
def edit_post(id):
    post = Post.query.get_or_404(id)
    post.title = request.json.get('title', post.title)
    post.body = request.json.get('body', post.body)
    post.img_url = request.json.get('img_url', post.img_url)

    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_json())


@main.route('/posts/<int:id>/active', methods=['POST'])
def post_deactivate(id):
    post = Post.query.get_or_404(id)
    post.active = request.json.get('active', post.active)

    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_json())
