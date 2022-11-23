try:
    from app import app
    import json
    import unittest
    from app.questions.model import MY_DATABASE

except Exception as e:
    print("some Modules are missing {}".format(e))
    
class FlaskTest(unittest.TestCase):

    # check for response 200
    def test_index(self):
        tester = app.test_client(self)
        
        response = tester.get("/api/v1/question")
        
        statuscode = response.status_code
        
        self.assertEqual(statuscode, 200)
    
    def test_index_content(self):
        tester = app.test_client(self)
        
        response = tester.get("/api/v1/question")
        
        self.assertEqual(response.content_type, "application/json")
        
    def test_non_existing_product(self):
        # test a non existing office
        tester = app.test_client(self)
        
        response = tester.get("/Api/v1/question/<quest_id>")
            
        self.assertEqual(response._status_code, 404)