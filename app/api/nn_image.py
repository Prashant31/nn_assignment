from flask import jsonify, request
import os
from . import api, UPLOAD_FOLDER
from .. import db
from ..models.nn_image import NnImage
from ..schemas.nn_image import nn_image_schema, nn_images_schema


@api.route('/nn_images', methods=['GET'])
def get_nn_images():
    pass


@api.route('/nn_images/<int:id>', methods=['GET'])
def get_nn_image(id):
    pass


@api.route('/nn_images', methods=['POST'])
def create_nn_image():
    success = []
    errors = []
    uploaded_files = request.files.getlist("images[]")
    if len(uploaded_files) < 1:
        return jsonify("Please Upload Atleast one file"), 400
    for up_file in uploaded_files:
        filename = up_file.filename
        try:
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            up_file.save(file_path)
            nn_image = NnImage(image_url=file_path, file_name=filename)
            db.session.add(nn_image)
            db.session.commit()
            success.append(nn_image_schema.dump(nn_image).data)
        except Exception as e:
            errors.append({"file_name": filename, "error" : str(e)})
    return jsonify({'success':success, 'errors':errors})


@api.route('/nn_images/<int:id>', methods=['DELETE'])
def delete_nn_image(id):
    pass
