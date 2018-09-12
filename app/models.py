from app import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, default=datetime.now().date())
    name = db.Column(db.String(50))

    def __repr__(self):
        return 'Post {}: {}'.format(self.id, self.body)
