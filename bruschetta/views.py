from flask import request, redirect, url_for, render_template, flash
from bruschetta import app, db
from bruschetta.models import Book, Category, Format


@app.route('/')
def index():
    books = Book.query.order_by(Book.id.desc()).all()
    return render_template('index.html', books=books)

@app.route('/book/add', methods=['GET', 'POST'])
def book_new():
    if request.method == 'POST':
        book = Book(
            title = request.form['title'],
            volume = request.form['volume'],
            series = request.form['series'],
            series_volume = request.form['series_volume'],
            author = request.form['author'],
            translator = request.form['translator'],
            publisher = request.form['publisher'],
            isbn = request.form['isbn'],
            published_on = request.form['published_on'],
            original_title = request.form['original_title'],
            note = request.form['note'],
            keyword = request.form['keyword'],
            disk = request.form['disk'])
        db.session.add(book)
        db.session.commit()
        flash('New book was successfully added.')
        return redirect(url_for('index'))
    else:
        return render_template('book_new.html')

@app.route('/book/<int:book_id>/')
def book_detail(book_id):
    book = Book.query.get(book_id)
    return render_template('book_detail.html', book=book)

@app.route('/categories/')
def category_list():
    categories = Category.query.all()
    return render_template('category_list.html', categories=categories)

@app.route('/category/add/', methods=['POST'])
def category_add():
    category = Category(name = request.form['name'])
    db.session.add(category)
    db.session.commit()
    return redirect(url_for('category_list'))

@app.route('/formats/')
def format_list():
    formats = Format.query.all()
    return render_template('format_list.html', formats=formats)

@app.route('/format/add/', methods=['POST'])
def format_add():
    fmt = Format(name = request.form['name'])
    db.session.add(fmt)
    db.session.commit()
    return redirect(url_for('format_list'))
