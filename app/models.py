from . import db
from datetime import datetime


class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    url = db.Column(db.String)

    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
