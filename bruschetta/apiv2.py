from flask import (
    Blueprint,
    request,
    jsonify,
)
from .models import db, Book, Category, Format, BookShelf
from .utils import str_to_bool


# Web API v2

bp = Blueprint("apiv2", __name__)


@bp.route("/books")
def books():
    offset = request.args.get("offset", default=0, type=int)
    limit = request.args.get("limit", default=100, type=int)
    include_disposed = str_to_bool(
        request.args.get("include_disposed", default="")
    )
    dataset = Book.query.order_by(Book.id.asc())
    if not include_disposed:
        dataset = dataset.filter_by(disposed=False)
    books = dataset.offset(offset).limit(limit).all()
    data = {"books": [b.to_dictionary() for b in books]}
    return jsonify({"status": "OK", "books": data})


@bp.route("/books/<int:book_id>")
def show_book(book_id):
    book = Book.query.get(book_id)
    data = {"books": []}
    if book is not None:
        data["books"].append(book.to_dictionary())
    return jsonify({"status": "OK", "books": data})


@bp.route("/books", methods=["POST"])
def add_book():
    category = Category.query.filter_by(name=request.json["category"]).first()
    fmt = Format.query.filter_by(name=request.json["format"]).first()
    book = Book(
        title=request.json["title"],
        volume=request.json["volume"],
        series=request.json["series"],
        series_volume=request.json["series_volume"],
        author=request.json["author"],
        translator=request.json["translator"],
        publisher=request.json["publisher"],
        category_id=category.id,
        format_id=fmt.id,
        isbn=request.json["isbn"],
        published_on=request.json["published_on"],
        original_title=request.json["original_title"],
        note=request.json["note"],
        keyword=request.json["keyword"],
        disk=request.json["disk"],
    )
    if request.json["disposed"] == "1":
        book.disposed = True
    db.session.add(book)
    db.session.commit()
    return jsonify({"status": "OK", "books": [book.to_dictionary()]})
