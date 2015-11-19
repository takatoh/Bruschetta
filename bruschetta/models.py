from bruschetta import db


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    volume = db.Column(db.String)
    author = db.Column(db.String)
    translator = db.Column(db.String)
    publisher = db.Column(db.String)

    def __repr__(self):
        return u'<Book title={id} title={title}>'.format(
            id=self.id, title=self.title)

def init():
    db.create_all()
