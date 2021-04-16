from app.exceptions import ValidatorError
from datetime import datetime

from . import db

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    body = db.Column(db.Text)
    img_url = db.Column(db.String(64))
    date_published = db.Column(db.DateTime(), default=datetime.utcnow)
    active = db.Column(db.Boolean, default=True)

    def to_json(self):
        json_post = {
            'title': self.title,
            'body': self.body.decode('utf-8'),
            'img_url': self.img_url,
            'date_published': self.date_published,
            'active': self.active,
        }
        return json_post

    @staticmethod
    def from_json(json_post):
        title = json_post.get('title')
        body = json_post.get('body')
        img_url = json_post.get('img_url')
        if body is None or body == '':
            raise ValidatorError('La publicacion no contiene datos que puedan ser almacenados')
        return Post(title=title, body=body, img_url=img_url)
