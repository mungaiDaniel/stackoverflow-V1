try:
    from app import app
    import unittest

except Exception as e:
    print("some Modules are missing {}".format(e))
    
class FlaskTest(unittest.TestCase):

    # check for response 200
    def test_index(self):
        tester = app.test_client(self)
        
        response = tester.get("/Api/v1/questions")
        
        statuscode = response.status_code
        
        self.assertEqual(statuscode, 200)
    
    def test_index_content(self):
        tester = app.test_client(self)
        
        response = tester.get("/Api/v1/questions")
        
        self.assertEqual(response.content_type, "application/json")
        
    def test_non_existing_product(self):
        # test a non existing office
        tester = app.test_client(self)
        
        response = tester.get("/Api/v1/question/<quest_id>")
            
        self.assertEqual(response._status_code, 404)
        
    def test_q4_data(self):
        tester = app.test_client(self)
        
        response = tester.get("/Api/v1/questions")
        
        self.assertTrue(b'q4' in response.data)
        
    def test_q3_data(self):
        tester = app.test_client(self)
        
        response = tester.get("/Api/v1/questions")
        
        self.assertTrue(b'q3' in response.data)
    def test_q2_data(self):
        tester = app.test_client(self)
        
        response = tester.get("/Api/v1/questions")
        
        self.assertTrue(b'q2' in response.data)
    def test_q1_data(self):
        tester = app.test_client(self)
        
        response = tester.get("/Api/v1/questions")
        
        self.assertTrue(b'q1' in response.data)