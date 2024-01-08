from app import db
from datetime import datetime
from timezone import UTC, JST


class Book(db.Model):
    __tablename__ = 'books'
    id             = db.Column(db.Integer, primary_key=True)
    title          = db.Column(db.String)
    volume         = db.Column(db.String)
    series         = db.Column(db.String)
    series_volume  = db.Column(db.String)
    author         = db.Column(db.String)
    translator     = db.Column(db.String)
    publisher      = db.Column(db.String)
    category_id    = db.Column(db.Integer, db.ForeignKey('categories.id'))
    format_id      = db.Column(db.Integer, db.ForeignKey('formats.id'))
    isbn           = db.Column(db.String)
    published_on   = db.Column(db.String)
    original_title = db.Column(db.String)
    note           = db.Column(db.String)
    keyword        = db.Column(db.String)
    disk           = db.Column(db.String)
    coverart_id    = db.Column(db.Integer, db.ForeignKey('coverarts.id'))
#    bookshelf_id   = db.Column(db.Integer, db.ForeignKey('bookshelves.id'))
    disposed       = db.Column(db.Boolean, default=False)
    created_at     = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Book title={self.id} title={self.title_with_vol()}>'

    def title_with_vol(self):
        if self.volume:
            return f'{self.title} [{self.volume}]'
        else:
            return self.title

    def to_dictionary(self):
        return {
            'id':             self.id,
            'title':          self.title,
            'volume':         self.volume,
            'series':         self.series,
            'series_volume':  self.series_volume,
            'author':         self.author,
            'translator':     self.translator,
            'publisher':      self.publisher,
            'category':       self.category.name,
            'format':         self.format.name,
            'isbn':           self.isbn,
            'published_on':   self.published_on,
            'original_title': self.original_title,
            'note':           self.note,
            'keyword':        self.keyword,
            'disk':           self.disk,
            'disposed':       self.disposed
        }

    def str_created_at(self):
        dt = self.created_at.replace(tzinfo=UTC()).astimezone(JST())
        return f'{dt:%Y-%m-%d %H:%M:%S}'


class Category(db.Model):
    __tablename__ = 'categories'
    id    = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String)
    books = db.relationship('Book', backref='category', lazy='dynamic')

    def __repr__(self):
        return f'<Category id={self.id} name={self.name}>'

    def to_dictionary(self):
        return {
            'id':   self.id,
            'name': self.name
        }


class Format(db.Model):
    __tablename__ = 'formats'
    id    = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String)
    books = db.relationship('Book', backref='format', lazy='dynamic')

    def __repr__(self):
        return f'<Format id={self.id} name={self.name}>'

    def to_dictionary(self):
        return {
            'id':   self.id,
            'name': self.name
        }


class CoverArt(db.Model):
    __tablename__ = 'coverarts'
    id       = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String)
    book = db.relationship('Book', backref='coverart', lazy='dynamic')

    def __repr__(self):
        return f'<CoverArt id={self.id} filename={self.filename}>'


#class BookShelf(db.Model):
#    __tablename__ = 'bookshelves'
#    id           = db.Column(db.Integer, primary_key=True)
#    name         = db.Column(db.String)
#    description  = db.Column(db.String)
#    books        = db.relationship('Book', backref='bookshelf', lazy='dynamic')

#    def __repr__(self):
#        return f'<BookShelf id={self.id} name={self.name}>'

#    def to_dictionary(self):
#        return {
#            'id':          self.id,
#            'name':        self.name,
#            'description': self.description
#        }


def init():
    db.create_all()
