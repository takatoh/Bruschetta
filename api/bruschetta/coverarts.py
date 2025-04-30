from flask import Blueprint


def create_blueprint(coverarts_dir):
    bp = Blueprint(
        "coverart",
        __name__,
        static_url_path="/coverart",
        static_folder=coverarts_dir,
    )
    return bp
