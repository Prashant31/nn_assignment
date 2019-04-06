from flask import Blueprint

api = Blueprint('api', __name__)

UPLOAD_FOLDER = '/TrainingImages'


# Import any endpoints here to make them available
from . import nn_image
from . import nn_model
