from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=True, unique=True)
    email = db.Column(db.String(255), unique=True)
    firstname = db.Column(db.String(255), unique=False)
    lastname = db.Column(db.String(255), unique=False)
