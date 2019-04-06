from marshmallow import Schema, fields


class NnExperimentSchema(Schema):

    class Meta:
        fields = ("learning_rate", "layers", "steps", "accuracy")


nn_experiment_schema = NnExperimentSchema()
nn_experiments_schema = NnExperimentSchema(many=True)
