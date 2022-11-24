from flask import make_response, jsonify, Blueprint, request

from app.answers.model import Answer

version1 = Blueprint('api-v1', __name__, url_prefix='/api/v1')

@version1.route('/answer', methods=['GET'])
def get():
    all_answers = Answer.get_all()
    
    return make_response(jsonify({
        "status": 200,
        "data": all_answers
    }), 200)
@version1.route('/answer', methods=['POST'])    
def post():
    data = request.get_json()
    title = data['title']
    description = data['description']
    
    new_answer = Answer(title=title, description=description)
    
    new_answer.save()
    
    return make_response(jsonify({
        "status": 201,
        "data": new_answer.json_dumps()
    }), 201)
    
@version1.route('/answer/<int:id>', methods=['GET'])
def get_by_id(id):
    answers = Answer.get_answer_by_id(id=id)
    if answers:
        return make_response(jsonify({
            "status": 200,
            "data": answers
        }), 200)
    return make_response(jsonify({
        "status": 404,
        "data": "No answe found with that id"
    }), 404)
    
@version1.route('/answer/<int:id>', methods=['PUT'])
def update(id):
    update_data = request.get_json()
    
    answer_to_edit = Answer.get_answer_by_id(id=id)[0]
    answer_to_edit = Answer.update_answer(update_data=update_data, id=id)
    
    return make_response(jsonify({
        "status": 201,
        "data": answer_to_edit
    }), 201)
    
@version1.route('/answer/<int:id>', methods=['DELETE'])
def delete(id):
    answer_to_delete = Answer.get_answer_by_id(id=id)
    if answer_to_delete:
        Answer.delete_answer(id=id)
        return make_response(jsonify({
            "status": 204,
            "message": "deleted successful"
        }))
        
    return make_response(jsonify({
        "status": 404,
        "error": "No answer found with that id"
    }))
    


    

    