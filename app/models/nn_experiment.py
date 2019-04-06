from .. import db


class NnExperiment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    learning_rate = db.Column(db.Float, nullable=False)
    layers = db.Column(db.Integer, nullable=False)
    steps = db.Column(db.Integer, nullable=False)
    accuracy = db.Column(db.Float, nullable=False)

    nn_model_id = db.Column(db.Integer, db.ForeignKey('nn_model.id'), nullable=False)
    nn_model = db.relationship('NnModel', backref=db.backref('experiments', lazy=True))

    # Additional fields

    def __repr__(self):
        return 'ExpId {}, i:{}, j:{}, k:{}, model:{}>'.format(self.id, self.learning_rate, self.layers, self.steps,
                                                              self.nn_model_id)
