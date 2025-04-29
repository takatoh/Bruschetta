from flask import Blueprint, request, jsonify, current_app
import os
from .models import db, Book, Category, Format, BookShelf, CoverArt
from .utils import str_to_bool, save_coverart, is_picture


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
    data = [b.to_dictionary() for b in books]
    return jsonify({"status": "OK", "books": data})


@bp.route("/books/<int:book_id>")
def show_book(book_id):
    book = Book.query.get(book_id)
    data = []
    if book is not None:
        data.append(book.to_dictionary())
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


@bp.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    category = Category.query.filter_by(name=request.json["category"]).first()
    fmt = Format.query.filter_by(name=request.json["format"]).first()
    if request.json["bookshelf"]:
        bookshelf_id = (
            BookShelf.query.filter_by(name=request.json["bookshelf"])
            .first()
            .id
        )
    else:
        bookshelf_id = None
    book = Book.query.get(book_id)
    book.title = request.json["title"]
    book.volume = request.json["volume"]
    book.series = request.json["series"]
    book.series_volume = request.json["series_volume"]
    book.author = request.json["author"]
    book.translator = request.json["translator"]
    book.publisher = request.json["publisher"]
    book.category_id = category.id
    book.format_id = fmt.id
    book.isbn = request.json["isbn"]
    book.published_on = request.json["published_on"]
    book.original_title = request.json["original_title"]
    book.note = request.json["note"]
    book.keyword = request.json["keyword"]
    book.disk = request.json["disk"]
    book.bookshelf_id = bookshelf_id
    book.disposed = request.json["disposed"]
    db.session.commit()
    return jsonify({"status": "OK", "books": [book.to_dictionary()]})


@bp.route("/coverarts/<int:book_id>", methods=["POST"])
def upload_coverart(book_id):
    book = Book.query.get(book_id)
    file = request.files["file"]
    if not is_picture(file.filename):
        return jsonify(
            {"status": "ERROR", "cause": "Looks like a not picture"}
        )
    tmp_filename = os.path.join(
        current_app.instance_path,
        current_app.config["TEMP_DIR"],
        file.filename,
    )
    file.save(tmp_filename)
    coverart_dir = os.path.join(
        current_app.instance_path, current_app.config["COVERARTS_DIR"]
    )
    coverart_filename = save_coverart(tmp_filename, coverart_dir)
    coverart = CoverArt(filename=coverart_filename)
    db.session.add(coverart)
    db.session.commit()
    book.coverart_id = coverart.id
    db.session.commit()
    os.remove(tmp_filename)
    return jsonify({"status": "OK", "books": [book.to_dictionary()]})


@bp.route("/coverarts/<int:book_id>", methods=["DELETE"])
def delete_coverart(book_id):
    book = Book.query.get(book_id)
    coverart = CoverArt.query.get(book.coverart_id)
    os.remove(
        os.path.join(
            current_app.instance_path,
            current_app.config["COVERARTS_DIR"],
            coverart.filename,
        )
    )
    book.coverart_id = None
    db.session.delete(coverart)
    db.session.commit()
    return jsonify({"status": "OK", "books": [book.to_dictionary()]})


@bp.route("/categories")
def list_categories():
    categories = Category.query.all()
    data = [c.to_dictionary() for c in categories]
    return jsonify({"status": "OK", "categories": data})


@bp.route("/categories", methods=["POST"])
def add_category():
    category = Category(name=request.json["name"])
    db.session.add(category)
    db.session.commit()
    return jsonify({"status": "OK", "categories": [category.to_dictionary()]})


@bp.route("/formats")
def list_formats():
    formats = Format.query.all()
    data = [f.to_dictionary() for f in formats]
    return jsonify({"status": "OK", "formats": data})


@bp.route("/formats", methods=["POST"])
def add_format():
    fmt = Format(name=request.json["name"])
    db.session.add(fmt)
    db.session.commit()
    return jsonify({"status": "OK", "formats": [fmt.to_dictionary()]})
