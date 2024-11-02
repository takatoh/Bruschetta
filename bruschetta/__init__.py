from flask import Flask
from flask_migrate import Migrate
from .models import db

__version__ = "v0.4.2"


def create_app(config_filename="./bruschetta.conf"):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    db.init_app(app)

    migrate = Migrate(app, db)

    from . import views

    app.register_blueprint(views.bp)

    from . import api

    app.register_blueprint(api.bp, url_prefix="/api")

    from . import coverarts

    app.register_blueprint(coverarts.bp)

    return app
