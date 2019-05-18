from flask import Flask
from flask_via import Via
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine

from .models import db


def create_app():
    app = Flask(__name__)
    app.config['VIA_ROUTES_MODULE'] = 'app.routes'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    if not database_exists(engine.url):
        create_database(engine.url)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    via = Via()
    via.init_app(app)
    return app

app = create_app()
