from .. import db


class NnModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'NnModel {}>'.format(self.id)
