from flask import Flask


app = Flask(__name__)

from .models import db

db.init_app(app)

app.config['VIA_ROUTES_MODULE'] = 'routes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from flask.ext.via import Via

via = Via()
via.init_app(app)

