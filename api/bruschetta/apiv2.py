from flask import Blueprint, request, jsonify, current_app
import os
import tempfile
from .models import db, Book, Category, Format, BookShelf, CoverArt
from .utils import str_to_bool, save_coverart, is_picture


# Web API v2

bp = Blueprint("apiv2", __name__)


@bp.route("/books")
def list_books():
    offset = request.args.get("offset", default=0, type=int)
    limit = request.args.get("limit", default=100, type=int)
    include_disposed = request.args.get(
        "include_disposed", default=False, type=str_to_bool
    )
    reverse_order = request.args.get(
        "reverse", default=False, type=str_to_bool
    )
    if reverse_order:
        dataset = Book.query.order_by(Book.id.desc())
    else:
        dataset = Book.query.order_by(Book.id.asc())
    if not include_disposed:
        dataset = dataset.filter_by(disposed=False)
    total_count = dataset.count()
    books = dataset.offset(offset).limit(limit).all()
    data = [b.as_dict() for b in books]
    count = len(data)
    return jsonify(
        {
            "status": "OK",
            "books": data,
            "count": count,
            "totalCount": total_count,
            "offset": offset,
        }
    )


@bp.route("/books/<int:book_id>")
def show_book(book_id):
    book = Book.query.get(book_id)
    if book is not None:
        book_details = book.as_dict()
        book_details = _set_coverart_url(book_details, request.host_url)
        return jsonify({"status": "OK", "books": [book_details]})
    else:
        return jsonify({"status": "Error", "cause": "Not found"})


@bp.route("/books", methods=["POST"])
def add_book():
    category = Category.query.filter_by(name=request.json["category"]).first()
    fmt = Format.query.filter_by(name=request.json["format"]).first()
    bookshelf = BookShelf.query.filter_by(name=request.json["bookshelf"]).first()
    book = Book(
        title=request.json["title"],
        volume=request.json["volume"],
        series=request.json["series"],
        series_volume=request.json["seriesVolume"],
        author=request.json["author"],
        translator=request.json["translator"],
        publisher=request.json["publisher"],
        category_id=category.id,
        format_id=fmt.id,
        isbn=request.json["isbn"],
        published_on=request.json["publishedOn"],
        original_title=request.json["originalTitle"],
        note=request.json["note"],
        keyword=request.json["keyword"],
        disk=request.json["disc"],
        bookshelf_id=bookshelf.id if bookshelf else None,
    )
    book.disposed = False
    db.session.add(book)
    db.session.commit()
    return jsonify({"status": "OK", "books": [book.as_dict()]})


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
    book.series_volume = request.json["seriesVolume"]
    book.author = request.json["author"]
    book.translator = request.json["translator"]
    book.publisher = request.json["publisher"]
    book.category_id = category.id
    book.format_id = fmt.id
    book.isbn = request.json["isbn"]
    book.published_on = request.json["publishedOn"]
    book.original_title = request.json["originalTitle"]
    book.note = request.json["note"]
    book.keyword = request.json["keyword"]
    book.disk = request.json["disc"]
    book.bookshelf_id = bookshelf_id
    book.disposed = request.json["disposed"]
    db.session.commit()
    book_details = _set_coverart_url(book.as_dict(), request.host_url)
    return jsonify({"status": "OK", "books": [book_details]})


@bp.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get(book_id)
    book.disposed = True
    db.session.commit()
    return jsonify({"status": "OK", "books": [book.as_dict()]})


@bp.route("/books/search")
def search_books():
    title = request.args.get("title")
    author = request.args.get("author")
    both = request.args.get("both")
    offset = request.args.get("offset", default=0, type=int)
    limit = request.args.get("limit", default=100, type=int)
    include_disposed = request.args.get(
        "inclde_disoposed", default=False, type=str_to_bool
    )
    reverse_order = request.args.get(
        "reverse", default=False, type=str_to_bool
    )
    if reverse_order:
        dataset = Book.query.order_by(Book.id.desc()).filter_by(
            disposed=include_disposed
        )
    else:
        dataset = Book.query.order_by(Book.id.asc()).filter_by(
            disposed=include_disposed
        )
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
    total_count = dataset.count()
    books = dataset.offset(offset).limit(limit).all()
    data = [b.as_dict() for b in books]
    count = len(data)
    return jsonify(
        {
            "status": "OK",
            "books": data,
            "count": count,
            "totalCount": total_count,
            "offset": offset,
        }
    )


@bp.route("/books/categorized/<int:category_id>")
def list_books_categorized(category_id):
    category = Category.query.get(category_id)
    books = Book.query.filter_by(category_id=category_id, disposed=False).all()
    data = [b.as_dict() for b in books]
    return jsonify({"status": "OK", "category": category.name, "books": data})


@bp.route("/books/disposed")
def list_books_disposed():
    offset = request.args.get("offset", default=0, type=int)
    limit = request.args.get("limit", default=100, type=int)
    dataset = Book.query.filter_by(disposed=True).order_by(Book.id.asc())
    books = dataset.offset(offset).limit(limit).all()
    data = [b.as_dict() for b in books]
    return jsonify({"status": "OK", "books": data})


@bp.route("/coverarts/<int:book_id>", methods=["POST"])
def upload_coverart(book_id):
    book = Book.query.get(book_id)
    file = request.files["file"]
    if not is_picture(file.filename):
        return jsonify(
            {"status": "ERROR", "cause": "Looks like a not picture"}
        )
    coverart_dir = os.path.join(
        current_app.instance_path, current_app.config["COVERARTS_DIR"]
    )
    with tempfile.NamedTemporaryFile(mode="w+b", delete=True) as tmp:
        tmp.write(file.read())
        coverart_filename = save_coverart(tmp.name, coverart_dir)
    coverart = CoverArt(filename=coverart_filename)
    db.session.add(coverart)
    db.session.commit()
    book.coverart_id = coverart.id
    db.session.commit()
    book_details = _set_coverart_url(book.as_dict(), request.host_url)
    return jsonify({"status": "OK", "books": [book_details]})


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
    return jsonify({"status": "OK", "books": [book.as_dict()]})


@bp.route("/categories")
def list_categories():
    categories = Category.query.all()
    data = [c.as_dict() for c in categories]
    return jsonify({"status": "OK", "categories": data})


@bp.route("/categories", methods=["POST"])
def add_category():
    category = Category(name=request.json["name"])
    db.session.add(category)
    db.session.commit()
    return jsonify({"status": "OK", "categories": [category.as_dict()]})


@bp.route("/formats")
def list_formats():
    formats = Format.query.all()
    data = [f.as_dict() for f in formats]
    return jsonify({"status": "OK", "formats": data})


@bp.route("/formats", methods=["POST"])
def add_format():
    fmt = Format(name=request.json["name"])
    db.session.add(fmt)
    db.session.commit()
    return jsonify({"status": "OK", "formats": [fmt.as_dict()]})


@bp.route("/bookshelves")
def list_bookshelves():
    bookshelves = BookShelf.query.all()
    data = [b.as_dict() for b in bookshelves]
    return jsonify({"status": "OK", "bookshelves": data})


@bp.route("/bookshelves/<int:bookshelf_id>")
def show_bookshelf(bookshelf_id):
    bookshelf = BookShelf.query.get(bookshelf_id)
    data = []
    if bookshelf is not None:
        data.append(bookshelf.as_dict())
    return jsonify({"status": "OK", "bookshelves": data})


@bp.route("/bookshelves", methods=["POST"])
def add_bookshelf():
    bookshelf = BookShelf(
        name=request.json["name"], description=request.json["description"]
    )
    db.session.add(bookshelf)
    db.session.commit()
    return jsonify({"status": "OK", "bookshelves": [bookshelf.as_dict()]})


@bp.route("/bookshelves/<int:bookshelf_id>", methods=["PUT"])
def update_bookshelf(bookshelf_id):
    bookshelf = BookShelf.query.get(bookshelf_id)
    bookshelf.name = request.json["name"]
    bookshelf.description = request.json["description"]
    db.session.commit()
    return jsonify({"status": "OK", "bookshelves": [bookshelf.as_dict()]})


def _set_coverart_url(book_details, host_url):
    coverart = book_details["coverart"]
    if len(coverart) > 0:
        book_details["coverart"] = f"{host_url}coverart/{coverart}"
    return book_details
