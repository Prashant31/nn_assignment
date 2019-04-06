from . import ModelSchema
from .nn_experiment import NnExperimentSchema
from marshmallow import fields
from ..models.nn_model import NnModel


class NnModelSchema(ModelSchema):
    experiments = fields.Nested(NnExperimentSchema, many=True)

    class Meta:
        fields = ("id", "name", "experiments")


nn_model_schema = NnModelSchema()
nn_models_schema = NnModelSchema(many=True)
