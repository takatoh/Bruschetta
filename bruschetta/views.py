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
            author = request.form['author'],
            translator = request.form['translator'],
            publisher = request.form['publisher'])
        db.session.add(book)
        db.session.commit()
        flash('New book was successfully added.')
        return redirect(url_for('index'))
    else:
        render_template('book_new.html')
