from bruschetta import db
from datetime import datetime
from bruschetta.timezone import UTC, JST


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
    disposed       = db.Column(db.Boolean, default=False)
    created_at     = db.Column(db.DateTime, default=datetime.utcnow)

    def title_with_vol(self):
        if self.volume:
            twv = self.title + ' [' + self.volume + ']'
        else:
            twv = self.title
        return twv

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
        return "{0:%Y-%m-%d %H:%M:%S}".format(dt)

    def __repr__(self):
        return u'<Book title={id} title={title}>'.format(
            id=self.id, title=self.title_with_vol())


class Category(db.Model):
    __tablename__ = 'categories'
    id    = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String)
    books = db.relationship('Book', backref='category', lazy='dynamic')

    def __repr__(self):
        return u'<Category id={id} name={name}>'.format(
            id=self.id, name=self.name)


class Format(db.Model):
    __tablename__ = 'formats'
    id    = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String)
    books = db.relationship('Book', backref='format', lazy='dynamic')

    def __repr__(self):
        return u'<Format id={id} name={name}>'.format(
            id=self.id, name=self.name)


class CoverArt(db.Model):
    __tablename__ = 'coverarts'
    id       = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String)


def init():
    db.create_all()
