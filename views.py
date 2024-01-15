from flask import request, redirect, url_for, render_template, flash, json, jsonify, Response
from sqlalchemy import or_
import requests
import os
from PIL import Image
import math
from app import app, db, __version__
from models import Book, Category, Format, CoverArt, BookShelf
from utils import str_to_bool, mk_filename, is_picture

BOOKS_PER_PAGE = 25


@app.route('/')
def index():
    return redirect('/books')

@app.route('/books')
def book_list():
    page = request.args.get('page')
    page = int(page) if page else 1
    limit = BOOKS_PER_PAGE
    offset = limit * (page - 1)
    search = request.args.get('search')
    q = Book.query.filter_by(disposed=False).order_by(Book.id.desc())
    if search:
        search = '%' + search + '%'
        q = q.filter(or_(Book.title.like(search), Book.author.like(search)))
    books = q.offset(offset).limit(limit).all()
    page_count = math.ceil(q.count() / limit)
    return render_template('books.html', books=books, page=page, page_count=page_count, version=__version__)

@app.route('/book/<int:book_id>')
def book_detail(book_id):
    book = Book.query.get(book_id)
    if book.coverart_id:
        coverart = CoverArt.query.get(book.coverart_id).filename
        coverart_url = '/coverart/' + coverart
    else:
        coverart_url = None
    return render_template('book_detail.html', book=book, coverart_url=coverart_url, version=__version__)

@app.route('/book/add', methods=['GET', 'POST'])
def book_add():
    if request.method == 'POST':
        category = Category.query.filter_by(name=request.form['category']).first()
        fmt = Format.query.filter_by(name=request.form['format']).first()
        book = Book(
            title          = request.form['title'],
            volume         = request.form['volume'],
            series         = request.form['series'],
            series_volume  = request.form['series_volume'],
            author         = request.form['author'],
            translator     = request.form['translator'],
            publisher      = request.form['publisher'],
            category_id    = category.id,
            format_id      = fmt.id,
            isbn           = request.form['isbn'],
            published_on   = request.form['published_on'],
            original_title = request.form['original_title'],
            note           = request.form['note'],
            keyword        = request.form['keyword'],
            disk           = request.form['disk'])
        db.session.add(book)
        db.session.commit()
        flash('New book was successfully added.')
        return redirect(url_for('index'))
    else:
        categories = Category.query.all()
        formats = Format.query.all()
        return render_template('book_add.html', categories=categories, formats=formats, version=__version__)

@app.route('/book/edit/<int:book_id>', methods=['GET', 'POST'])
def book_edit(book_id):
    if request.method == 'POST':
        category = Category.query.filter_by(name=request.form['category']).first()
        fmt = Format.query.filter_by(name=request.form['format']).first()
        bookshelf = BookShelf.query.filter_by(name=request.form['bookshelf']).first()
        book = Book.query.get(book_id)
        book.title          = request.form['title']
        book.volume         = request.form['volume']
        book.series         = request.form['series']
        book.series_volume  = request.form['series_volume']
        book.author         = request.form['author']
        book.translator     = request.form['translator']
        book.publisher      = request.form['publisher']
        book.category_id    = category.id
        book.format_id      = fmt.id
        book.isbn           = request.form['isbn']
        book.published_on   = request.form['published_on']
        book.original_title = request.form['original_title']
        book.note           = request.form['note']
        book.keyword        = request.form['keyword']
        book.disk           = request.form['disk']
        book.bookshelf_id   = bookshelf.id
        if len(request.form.getlist('disposed')) == 1:
            book.disposed = True
        else:
            book.disposed = False
        db.session.commit()
        flash('The book was successfully updated.')
        return redirect(url_for('book_detail', book_id=book_id))
    else:
        book = Book.query.get(book_id)
        categories = Category.query.all()
        formats = Format.query.all()
        bookshelves = BookShelf.query.all()
        return render_template('book_edit.html', book=book, categories=categories, formats=formats, bookshelves=bookshelves, version=__version__)

@app.route('/book/fetch_coverart/<int:book_id>', methods=['GET', 'POST'])
def book_fetch_coverart(book_id):
    if request.method == 'POST':
        book = Book.query.get(book_id)
        isbn = book.isbn
        r = requests.get('https://api.openbd.jp/v1/get?isbn=' + isbn)
        book_info = r.json()
        if not book_info[0]:
            flash('Failed to get book infomations from OpenBD.')
            return redirect(url_for('book_detail', book_id=book_id))
        coverart_url = book_info[0]['summary']['cover']
        if not coverart_url:
            flash('Not found cover art on OpenBD.')
            return redirect(url_for('book_detail', book_id=book_id))
        filename = 'isbn-' + coverart_url.split('/')[-1]
        r = requests.get(coverart_url)
        with open(os.path.join(app.config['COVERARTS_DIR'], filename), 'wb') as f:
            f.write(r.content)
        coverart = CoverArt(filename = filename)
        db.session.add(coverart)
        db.session.commit()
        book.coverart_id = coverart.id
        db.session.commit()
        return redirect(url_for('book_detail', book_id=book_id))
    else:
        book = Book.query.get(book_id)
        return render_template('book_fetch_coverart.html', book=book, version=__version__)

@app.route('/book/upload_coverart/<int:book_id>', methods=['GET', 'POST'])
def book_upload_coverart(book_id):
    if request.method == 'POST':
        book = Book.query.get(book_id)
        file = request.files['file']
        if not is_picture(file.filename):
            flash('Looked like non-picture file.')
            return redirect(url_for('book_detail', book_id=book_id))
        tmp_filename = os.path.join(app.config['TEMP_DIR'], file.filename)
        file.save(tmp_filename)
        coverart_filename = save_coverart(tmp_filename)
        coverart = CoverArt(filename = coverart_filename)
        db.session.add(coverart)
        db.session.commit()
        book.coverart_id = coverart.id
        db.session.commit()
        os.remove(tmp_filename)
        return redirect(url_for('book_detail', book_id=book_id))
    else:
        book = Book.query.get(book_id)
        return render_template('book_upload_coverart.html', book=book, version=__version__)

@app.route('/book/delete_coverart/<int:book_id>')
def book_delete_coverart(book_id):
    book = Book.query.get(book_id)
    coverart = CoverArt.query.get(book.coverart_id)
    os.remove(os.path.join(app.config['COVERARTS_DIR'], coverart.filename))
    book.coverart_id = None
    db.session.delete(coverart)
    db.session.commit()
    return redirect(url_for('book_detail', book_id=book_id))

@app.route('/book/disposed')
def book_list_disposed():
    page = request.args.get('page')
    page = int(page) if page else 1
    limit = BOOKS_PER_PAGE
    offset = limit * (page - 1)
    q = Book.query.filter_by(disposed=True).order_by(Book.id.desc())
    books = q.offset(offset).limit(limit).all()
    page_count = math.ceil(q.count() / limit)
    return render_template('book_list_disposed.html', books=books, page=page, page_count=page_count, version=__version__)

@app.route('/book/categorized/<int:category_id>')
def book_list_categorized(category_id):
    category = Category.query.get(category_id)
    books = Book.query.filter_by(category_id=category_id, disposed=False).all()
    return render_template('book_categorized.html', category=category, books=books, version=__version__)

@app.route('/categories')
def category_list():
    categories = Category.query.all()
    return render_template('category_list.html', categories=categories, version=__version__)

@app.route('/category/add', methods=['GET', 'POST'])
def category_add():
    if request.method == 'POST':
        category = Category(name = request.form['name'])
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('category_list'))
    else:
        return render_template('category_add.html', version=__version__)

@app.route('/formats')
def format_list():
    formats = Format.query.all()
    return render_template('format_list.html', formats=formats, version=__version__)

@app.route('/format/add', methods=['GET', 'POST'])
def format_add():
    if request.method == 'POST':
        fmt = Format(name = request.form['name'])
        db.session.add(fmt)
        db.session.commit()
        return redirect(url_for('format_list'))
    else:
        return render_template('format_add.html', version=__version__)

@app.route('/bookshelves')
def bookshelf_list():
    bookshelves = BookShelf.query.all()
    return render_template('bookshelf_list.html', bookshelves=bookshelves, version=__version__)

@app.route('/bookshelf/add', methods=['GET', 'POST'])
def bookshelf_add():
    if request.method == 'POST':
        bookshelf = BookShelf(name=request.form['name'], description=request.form['description'])
        db.session.add(bookshelf)
        db.session.commit()
        return redirect(url_for('bookshelf_list'))
    else:
        return render_template('bookshelf_add.html', version=__version__)

@app.route('/bookshelf/<int:bookshelf_id>')
def bookshelf_detail(bookshelf_id):
    bookshelf = BookShelf.query.get(bookshelf_id)
    return render_template('bookshelf_detail.html', bookshelf=bookshelf, version=__version__)

@app.route('/bookshelf/edit/<int:bookshelf_id>', methods=['GET', 'POST'])
def bookshelf_edit(bookshelf_id):
    if request.method == 'POST':
        bookshelf = BookShelf.query.get(bookshelf_id)
        bookshelf.name        = request.form['name']
        bookshelf.description = request.form['description']
        db.session.commit()
        flash('The bookshelf was successfully updated.')
        return redirect(url_for('bookshelf_detail', bookshelf_id=bookshelf_id))
    else:
        bookshelf = BookShelf.query.get(bookshelf_id)
        return render_template('bookshelf_edit.html', bookshelf=bookshelf, version=__version__)

@app.route('/coverart/<filename>')
def coverart(filename):
    path = os.path.join(app.config['COVERARTS_DIR'], filename)
    with open(path, 'rb') as f:
        content = f.read()
    return Response(content, mimetype='image/jpeg')


# Web API

@app.route('/api/books')
def api_books():
    offset = request.args.get('offset', default=0, type=int)
    limit = request.args.get('limit', default=100, type=int)
    include_disposed = str_to_bool(request.args.get('include_disposed', default=''))
    dataset = Book.query.order_by(Book.id.asc())
    if not include_disposed:
        dataset = dataset.filter_by(disposed=False)
    books = dataset.offset(offset).limit(limit).all()
    data = { 'books': [ b.to_dictionary() for b in books ] }
    return jsonify(data)

@app.route('/api/book/<int:book_id>')
def api_book(book_id):
    book = Book.query.get(book_id)
    data = { 'books': [] }
    if not book is None:
        data['books'].append(book.to_dictionary())
    return jsonify(data)

@app.route('/api/book/add', methods=['POST'])
def api_book_add():
    category = Category.query.filter_by(name=request.json['category']).first()
    fmt = Format.query.filter_by(name=request.json['format']).first()
    book = Book(
        title          = request.json['title'],
        volume         = request.json['volume'],
        series         = request.json['series'],
        series_volume  = request.json['series_volume'],
        author         = request.json['author'],
        translator     = request.json['translator'],
        publisher      = request.json['publisher'],
        category_id    = category.id,
        format_id      = fmt.id,
        isbn           = request.json['isbn'],
        published_on   = request.json['published_on'],
        original_title = request.json['original_title'],
        note           = request.json['note'],
        keyword        = request.json['keyword'],
        disk           = request.json['disk']
        )
    if request.json['disposed'] == '1':
        book.disposed = True
    db.session.add(book)
    db.session.commit()
    return jsonify({ 'status' : 'OK', 'books' : [ book.to_dictionary() ] })

@app.route('/api/search')
def api_search():
    title = request.args.get('title')
    author = request.args.get('author')
    both = request.args.get('both')
    dataset = Book.query.order_by(Book.id.asc()).filter_by(disposed=False)
    if both:
        both = '%' + both + '%'
        dataset = dataset.filter(Book.title.like(both) | Book.author.like(both))
    else:
        if title:
            dataset = dataset.filter(Book.title.like('%' + title + '%'))
        if author:
            dataset = dataset.filter(Book.author.like('%' + author + '%'))
    books = dataset.all()
    data = { 'books' : [ b.to_dictionary() for b in books ] }
    return jsonify(data)

@app.route('/api/categories')
def api_category_list():
    categories = Category.query.all()
    data = { 'categories' : [ c.to_dictionary() for c in categories ] }
    return jsonify(data)

@app.route('/api/formats')
def api_format_list():
    formats = Format.query.all()
    data = { 'formats' : [ f.to_dictionary() for f in formats ] }
    return jsonify(data)

@app.route('/api/bookshelves')
def api_bookshelf_list():
    bookshelves = BookShelf.query.all()
    data = { 'bookshelves' : [ b.to_dictionary() for b in bookshelves ] }
    return jsonify(data)

@app.route('/api/bookshelf/<int:bookshelf_id>')
def api_bookshelf(bookshelf_id):
    bookshelf = BookShelf.query.get(bookshelf_id)
    data = { 'bookshelves': [] }
    if not bookshelf is None:
        data['bookshelves'].append(bookshelf.to_dictionary())
    return jsonify(data)


# Functions

def save_coverart(tmp_filename):
    coverart_filename = mk_filename()
    while os.path.isfile(os.path.join(app.config['COVERARTS_DIR'], coverart_filename)):
        coverart_filename = mk_filename()
    img = Image.open(tmp_filename)
    img.thumbnail((300, 300))
    img = img.convert('RGB')
    img.save(os.path.join(app.config['COVERARTS_DIR'], coverart_filename))
    return coverart_filename
