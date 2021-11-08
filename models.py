from db import db

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)


    def to_json(self):
        return {'id': self.id, 'title': self.title, 'author': self.author}
