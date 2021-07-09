from db import db

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {'username':self.username, 'password': self.password}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
