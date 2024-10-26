from flask import (
    Blueprint,
    request,
    jsonify,
)
from app import db
from models import Book, Category, Format, BookShelf
from utils import str_to_bool


# Web API

bp = Blueprint("api", __name__)


@bp.route("/books")
def api_books():
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
    return jsonify(data)


@bp.route("/book/<int:book_id>")
def api_book(book_id):
    book = Book.query.get(book_id)
    data = {"books": []}
    if book is not None:
        data["books"].append(book.to_dictionary())
    return jsonify(data)


@bp.route("/book/add", methods=["POST"])
def api_book_add():
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


@bp.route("/search")
def api_search():
    title = request.args.get("title")
    author = request.args.get("author")
    both = request.args.get("both")
    dataset = Book.query.order_by(Book.id.asc()).filter_by(disposed=False)
    if both:
        both = "%" + both + "%"
        dataset = dataset.filter(
            Book.title.like(both) | Book.author.like(both)
        )
    else:
        if title:
            dataset = dataset.filter(Book.title.like("%" + title + "%"))
        if author:
            dataset = dataset.filter(Book.author.like("%" + author + "%"))
    books = dataset.all()
    data = {"books": [b.to_dictionary() for b in books]}
    return jsonify(data)


@bp.route("/categories")
def api_category_list():
    categories = Category.query.all()
    data = {"categories": [c.to_dictionary() for c in categories]}
    return jsonify(data)


@bp.route("/formats")
def api_format_list():
    formats = Format.query.all()
    data = {"formats": [f.to_dictionary() for f in formats]}
    return jsonify(data)


@bp.route("/bookshelves")
def api_bookshelf_list():
    bookshelves = BookShelf.query.all()
    data = {"bookshelves": [b.to_dictionary() for b in bookshelves]}
    return jsonify(data)


@bp.route("/bookshelf/<int:bookshelf_id>")
def api_bookshelf(bookshelf_id):
    bookshelf = BookShelf.query.get(bookshelf_id)
    data = {"bookshelves": []}
    if bookshelf is not None:
        data["bookshelves"].append(bookshelf.to_dictionary())
    return jsonify(data)
