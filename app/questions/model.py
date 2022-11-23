""" questions model """

MY_DATABASE = {
    "questions": [],
    }

Questions = MY_DATABASE["questions"]

class Data:
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
