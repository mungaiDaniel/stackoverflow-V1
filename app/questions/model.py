""" questions model """

MY_DATABASE = {
    "questions": [],
    }

Questions = MY_DATABASE["questions"]

class Question:
    def __init__(self, description, title):
        self.id = len(Questions) + 1
        self.title = title
        self.description = description
        
    def json_dumps(self):
        question = {
            "id": self.id,
            "title": self.title,
            "description": self.description
        }
        
        return question
    
    def save(self):
        Questions.append(self)
        return self.json_dumps()
    
    @classmethod
    def get_all(cls):
        
        output = []
        
        for question in Questions:
            output.append(question.json_dumps())
        
        return output
    
    @classmethod
    def get_question_by_id(cls, id):
        output = []
        for question in Questions:
            if question.id == id:
                output.append(question.json_dumps())
                return question.json_dumps()
            
    @staticmethod
    def update_question(my_data, id):
        for question in Questions:
            if question.id == id:
                question.title = my_data["title"]
                question.description = my_data["description"]
        return [{
            "id": id,
            "title": my_data["title"],
            "description": my_data["description"]
        }]
        
    @classmethod
    def delete_question(cls, id):
        
        for question in Questions:
            if question.id == id:
                Questions.remove(question)
                

