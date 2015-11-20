from flask import request, redirect, url_for, render_template, flash
from bruschetta import app, db
from bruschetta.models import Book


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
