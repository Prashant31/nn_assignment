from . import ModelSchema
from ..models.nn_image import NnImage


class NnImageSchema(ModelSchema):

    class Meta:
        model = NnImage


nn_image_schema = NnImageSchema()
nn_images_schema = NnImageSchema(many=True)
