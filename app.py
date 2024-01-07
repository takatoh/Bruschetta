from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

__version__ = 'v0.4-alpha'


app = Flask(__name__)
app.config.from_pyfile('./bruschetta.conf')

db = SQLAlchemy(app)

import models

migrate = Migrate(app, db)

import views
