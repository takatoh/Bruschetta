from flask import Flask
import os
from .models import init_app, db

__version__ = "v0.4.2"


def create_app(config_filename="./bruschetta.conf"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    init_app(app)
    db.init_app(app)

    from . import views

    app.register_blueprint(views.bp)

    from . import api

    app.register_blueprint(api.bp, url_prefix="/api")

    from . import coverarts

    coverarts_dir = os.path.join(
        app.instance_path, app.config["COVERARTS_DIR"]
    )
    app.register_blueprint(coverarts.create_blueprint(coverarts_dir))

    return app
