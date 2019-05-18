
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    firstname = db.Column(db.String(255), unique=False)
    lastname = db.Column(db.String(255), unique=False)

    def __repr__(self):
        return f"User('{self.id}','{self.email}','{self.firstname}','{self.lastname}')"

