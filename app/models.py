from . import db
from datetime import datetime


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    images = db.relationship('Image', backref='cate', lazy='dynamic')
    count = db.Column(db.Integer, default=0)
    conver_url = db.Column(db.String)

    def add_one(self, filename):
        if self.count:
            self.count += 1
        else:
            # init value as integer
            self.count = 1
            self.conver_url = filename


class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    url = db.Column(db.String)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
