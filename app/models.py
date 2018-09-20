from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    bio = db.Column(db.String(140))
    url = db.Column(db.String(100))
    username = db.Column(db.String(50), unique=True, index=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(256))
    posts = db.relationship("Post",
                    backref=db.backref("post", lazy="joined"))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return (self.user_id)

    def __repr__(self):
        return 'User {} is {} years old. Bio - {}'.format(self.name, self.age, self.bio)


class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    tweet = db.Column(db.String(140))
    date_posted = db.Column(db.DateTime, default=datetime.now().date())
    likes = db.Column(db.Integer)

    def __repr__(self):
        return 'Post {}: {}'.format(self.id, self.tweet)


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
