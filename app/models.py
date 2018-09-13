from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    bio = db.Column(db.String(50))
    url = db.Column(db.String(100))

    def __repr__(self):
        return 'User {} is {} years old. Bio - {}'.format(self.name, self.age, self.bio)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, default=datetime.now().date())
    name = db.Column(db.String(50))

    def __repr__(self):
        return 'Post {}: {}'.format(self.id, self.tweet)
