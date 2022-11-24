""" Answer model """

MY_ANSWER_DATABASE = {
    "answers": [],
}
Answers = MY_ANSWER_DATABASE["answers"]

class Answer:
    def __init__(self, description, title):
        self.id = len(Answers) + 1
        self.title = title
        self.description = description
        
    def json_dumps(self):
        answer = {
            "id": self.id,
            "title": self.title,
            "description": self.description
        }
        
        return answer
    
    def save(self):
        Answers.append(self)
        return self.json_dumps()
    
    @classmethod
    def get_all(cls):
        
        output = []
        
        for answer in Answers:
            output.append(answer.json_dumps())
        
        return output
    
    @classmethod
    def get_answer_by_id(cls, id):
        output = []
        for answer in Answers:
            if answer.id == id:
                output.append(answer.json_dumps())
                return { "data": output}
            
    @staticmethod
    def update_answer(update_data, id):
        for answer in Answers:
            if answer.id == id:
                answer.title = update_data["title"]
                answer.description = update_data["description"]
                
        return [{
            "id": id,
            "title": update_data["title"],
            "description": update_data["description"]
        }]
    
    @classmethod
    def delete_answer(cls, id):
        
        for answer in Answers:
            if answer.id == id:
                Answers.remove(answer)
                
