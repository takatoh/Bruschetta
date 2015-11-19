from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('bruschetta.config')

db = SQLAlchemy(app)

import bruschetta.views
