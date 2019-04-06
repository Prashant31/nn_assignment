from flask import jsonify, request
import os
from . import api, UPLOAD_FOLDER
from .. import db
from ..models.nn_model import NnModel
from ..models.nn_experiment import NnExperiment
from ..models.nn_image import NnImage
from ..schemas.nn_model import nn_model_schema, nn_models_schema


@api.route('/nn_models', methods=['GET'])
def get_nn_models():
    all_models = NnModel.query.all()
    return jsonify(nn_models_schema.dump(all_models).data)


@api.route('/nn_models/<int:id>', methods=['GET'])
def get_nn_model(id):
    model = NnModel.query.get(id)
    return jsonify(nn_model_schema.dump(model).data)


@api.route('/nn_models', methods=['POST'])
def create_nn_model():
    new_model = NnModel.query.filter_by(name=request.json['name']).first()
    if new_model is None:
        new_model = NnModel(request.json['name'])
        db.session.add(new_model)
        db.session.commit()
        return jsonify({"name": new_model.name})
    else:
        return jsonify({"error": "Model with Name already Exists"})


@api.route('/nn_models/<int:id>/train', methods=['GET'])
def train_model(id):
    from ..services import train
    model = NnModel.query.get(id)
    if model is None:
        return jsonify("Model With Given Id foes not exist"), 400
    for i in [0.001, 0.01, 0.1]:
        for j in [1, 2, 4]:
            for k in [1000,2000,4000]:
                nn_experiment = NnExperiment.query.filter_by(learning_rate=i, layers=j, steps=k, nn_model=model).first()
                if nn_experiment is None:
                    acc = train(i, j, k, UPLOAD_FOLDER)
                    nn_experiment = NnExperiment(learning_rate=i, layers=j, steps=k, accuracy=acc, nn_model=model)
                    db.session.add(nn_experiment)
                    db.session.commit()
    return jsonify(nn_model_schema.dump(model).data)


@api.route('/nn_models/<int:id>/test', methods=['POST'])
def test_model(id):
    from ..services import test
    model = NnModel.query.get(id)
    if model is None:
        return jsonify("Model With Given Id foes not exist"), 400
    # Save Train File may not be necessary
    up_file = request.files.get('image', None)
    if up_file is None:
        return jsonify("Please upload a training Image"), 400
    file_path = os.path.join(UPLOAD_FOLDER, up_file.filename)
    up_file.save(file_path)
    nn_exp = NnExperiment.query.filter_by(nn_model_id=model.id).order_by(NnExperiment.accuracy.desc()).first()
    if nn_exp is None:
        return jsonify("Model Not Trained Yet")
    acc = test(nn_exp.learning_rate, nn_exp.layers, nn_exp.steps, file_path)
    return jsonify({"accuracy": acc})



