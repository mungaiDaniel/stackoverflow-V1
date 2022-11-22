from flask import Flask, request
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app)

Questions = {
        'q1':{
            'Question_1': 'Spring Integration: Define sequential handling of messages using Java DSL'
        },
        'q2':{
            'Question_2': 'Spring Integration: Define sequential handling of messages using Java DSL'
        },
        'q3':{
            'Question_3': 'Spring Integration: Define sequential handling of messages using Java DSL'
        },
        'q4':{
            'Question_4': 'Spring Integration: Define sequential handling of messages using Java DSL'
        } 
}

def abort_if_question_doesnt_exsit(quest_id):
    if quest_id not in Questions:
        abort(404, message="question {} doesn't exist".format(quest_id))

parse = reqparse.RequestParser()
parse.add_argument('question', type=str, help='questions')

class Question(Resource):
    def get(self, quest_id):
        abort_if_question_doesnt_exsit(quest_id)
        return Questions[quest_id]
    
class QuestionList(Resource):
    def get(self):
        return Questions
    
api.add_resource(QuestionList, '/Api/v1/questions')
api.add_resource(Question, '/Api/v1/question/<quest_id>')




if __name__ == "__main__":
    app.run(debug=True)
