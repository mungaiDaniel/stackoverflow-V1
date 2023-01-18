""" views """

from flask import make_response, jsonify, Blueprint, request
import json

from app.questions.model import Question

V1 = Blueprint('api-version1', __name__, url_prefix='/api/v1')

@V1.route('/question', methods=['GET'])
def get():
    
    questions = Question.get_all()

    return make_response(jsonify({
        "status": 200,
        "data": questions
    }), 200)
    
@V1.route('/question', methods=['POST'])
def post():
    
    data = request.get_json()
    if not request.json or not 'title' in request.json or not 'description' in request.json:
        return make_response(jsonify({
            "status": 400,
            "error": "details name is required"
        }), 400)
    title = data["title"]
    description = data["description"]
        
    new_question = Question(title=title, description=description)
    
    new_question.save()
    return make_response(jsonify({
        "status": 201,
        "data": new_question.json_dumps()
    }), 201)
    
@V1.route('/question/<int:id>', methods=['GET'])
def get_by_id(id):
    
    question = Question.get_question_by_id(id=id)
    
    if question:
        return make_response(jsonify({
            "status": 200,
            "data": question
        }), 200)
    return make_response(jsonify({
        "status": 404,
        "data": "No question was found by that id"
    }), 404)
    
@V1.route('/question/<int:id>', methods=['DELETE'])
def delete(id):
    question_to_delete = Question.get_question_by_id(id=id)
    
    if question_to_delete:
        
        Question.delete_question(id=id)
        
        return make_response(jsonify({
            "status": 204,
            "message": "deleted successful"
        }), 204)
            
            
    return make_response(jsonify({
        "status": 404,
        "error": "No question found with that id"
     }), 404)
    
@V1.route('/question/<int:id>', methods=['PUT'])
def update(id):
    
    my_data = request.get_json()
    
    question_to_edit = Question.get_question_by_id(id=id)
    question_to_edit = Question.update_question(my_data=my_data, id=id)
    
    return make_response(jsonify({
        "status": 201,
        "data": question_to_edit
    }), 201)