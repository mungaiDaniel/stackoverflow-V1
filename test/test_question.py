from unittest import TestCase
from app.questions.model import MY_DATABASE

from app.app import app
import json
from app.utils.helper import question1_to_post, question2_to_post, question3_to_post, question4_to_post, question5_to_post
    
class TestAnswer(TestCase):
    def setUp(self):
        
        client = app.test_client()
        
        self.client = client
        
    def tearDown(self):
        MY_DATABASE["questions"].clear()
    
    def post_question(self):
        response = self.client.post(path='api/v1/question', data=json.dumps(question1_to_post),
                                    content_type='application/json')
        return response
    
    
    def test_create_question(self):
         with self.client:
             response = self.post_question()
             
             self.assertEqual(response.status_code, 201)
             response = self.client.post('api/v1/question', data=json.dumps(question1_to_post),
                                         headers = {'content-type': 'application' '/json'})
             self.assertEqual(response.status_code, 201)
             
    def test_question_with_no_title(self):
         with self.client:
             
             response = self.client.post('api/v1/question', data=json.dumps(question2_to_post),
                                         headers = {'content-type': 'application' '/json'})
             self.assertEqual(response.status_code, 201)    
             
    def test_delete_question(self):
        self.post_question()
        
        response = self.client.delete('api/v1/question/1', headers = {'content-type': 'application' '/json'})
        
        self.assertEqual(response.status_code, 204)
     
    def test_question_with_no_title(self):
         with self.client:
             response = self.post_question()
            
             
             response = self.client.post('api/v1/question', data=json.dumps(question4_to_post),
                                         headers = {'content-type': 'application' '/json'})
             self.assertEqual(response.status_code, 400)  
             
    def test_question_with_no_description(self):
         with self.client:
             response = self.post_question()
            
             
             response = self.client.post('api/v1/question', data=json.dumps(question5_to_post),
                                         headers = {'content-type': 'application' '/json'})
             self.assertEqual(response.status_code, 400) 
            