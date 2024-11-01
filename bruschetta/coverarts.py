from flask import Blueprint
from app import app


bp = Blueprint(
    "coverart",
    __name__,
    static_url_path="/coverart",
    static_folder=app.config["COVERARTS_DIR"],
)
