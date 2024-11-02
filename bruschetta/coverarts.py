from flask import Blueprint, current_app


bp = Blueprint(
    "coverart",
    __name__,
    static_url_path="/coverart",
    static_folder=current_app.config["COVERARTS_DIR"],
)
