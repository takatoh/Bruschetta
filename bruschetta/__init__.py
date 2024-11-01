from flask import Flask
from flask_migrate import Migrate
from .models import db

__version__ = "v0.4.2"


app = Flask(__name__)
app.config.from_pyfile("./bruschetta.conf")

db.init_app(app)

migrate = Migrate(app, db)

from . import views

app.register_blueprint(views.bp)

from . import api

app.register_blueprint(api.bp, url_prefix="/api")

from . import coverarts

app.register_blueprint(coverarts.bp)
