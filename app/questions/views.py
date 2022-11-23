""" views """

from flask import make_response, jsonify, Blueprint, request
import json

from app.questions.model import Data

V1 = Blueprint('api-version1', __name__, url_prefix='/api/v1')

@V1.route('/question', methods=['GET'])
def get():
    
    questions = Data.get_all()
    
    return make_response(jsonify({
        "status": 200,
        "data": questions
    }), 200)
    
@V1.route('/question', methods=['POST'])
def post():
    data = request.get_json()
    title = data["title"]
    description = data["description"]
    
    new_question = Data(title=title, description=description)
    
    new_question.save()
    return make_response(jsonify({
        "status": 201,
        "data": new_question.json_dumps()
    }), 201)