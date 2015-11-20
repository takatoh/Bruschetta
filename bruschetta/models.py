from bruschetta import db


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
    isbn           = db.Column(db.String)
    published_on   = db.Column(db.String)
    original_title = db.Column(db.String)
    note           = db.Column(db.String)
    keyword        = db.Column(db.String)
    disk           = db.Column(db.String)
    disposed       = db.Column(db.Boolean)

    def title_with_vol(self):
        if self.volume == '':
            twv = self.title
        else:
            twv = self.title + ' [' + self.volume + ']'
        return twv

    def __repr__(self):
        return u'<Book title={id} title={title}>'.format(
            id=self.id, title=self.title_with_vol())

def init():
    db.create_all()
