from .. import db


class NnImage(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(1000), nullable=False)
    image_url = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return 'ImgId: {}, Url:{}>'.format(self.id, self.image_url)
