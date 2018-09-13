from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    bio = db.Column(db.String(50))
    url = db.Column(db.String(100))
    username = db.Column(db.String(30), index=True, unique=True)
    email = db.Column(db.String(50), index=True, unique=True)
    password_hash = db.Column(db.String(256))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User {} is {} years old. Bio - {}'.format(self.name, self.age, self.bio)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, default=datetime.now().date())
    name = db.Column(db.String(50))

    def __repr__(self):
        return 'Post {}: {}'.format(self.id, self.tweet)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
