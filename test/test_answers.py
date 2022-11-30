from unittest import TestCase
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from app.answers.model import MY_ANSWER_DATABASE

from app.app import app
import json
from app.utils.helper import answer1_to_post, answer2_to_post, answer3_to_post,question1_to_post, answer4_to_post
    
class TestAnswer(TestCase):
    def setUp(self):
        
        client = app.test_client()
        
        self.client = client
        
    def tearDown(self):
        MY_ANSWER_DATABASE["answers"].clear()
    
    def post_answer(self):
        response = self.client.post(path='api/v1/answer/1', data=json.dumps(answer1_to_post),
                                    content_type='application/json')
        return response
    
    def post_question(self):
        response = self.client.post(path='api/v1/question', data=json.dumps(question1_to_post),
                                content_type='application/json')
        return response
        
    def test_create_answer(self):
         with self.client:
             response1 = self.post_question()
             self.assertEqual(response1.status_code, 201)
             response = self.post_answer()
             
             self.assertEqual(response.status_code, 201)
             response = self.client.post('api/v1/answer/1', data=json.dumps(answer1_to_post),
                                         headers = {'content-type': 'application' '/json'})
             self.assertEqual(response.status_code, 201)
    
    def test_answer_with_no_title(self):
         with self.client:
             response1 = self.post_question()
            
             
             response = self.client.post('api/v1/answer/1', data=json.dumps(answer3_to_post),
                                         headers = {'content-type': 'application' '/json'})
             self.assertEqual(response.status_code, 400)    
                  
    
    def test_get_answers(self):
        with self.client:
            response = self.client.get('/api/v1/answers/1')
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response.json['data'], list)
            
    def test_get_an_answers(self):
        with self.client:
            response = self.client.get('/api/v1/answer')
            self.assertEqual(response.status_code, 200)
            
    def test_get_an_answers(self):
        with self.client:
            response = self.client.get('/api/v1/answer/1')
            self.assertEqual(response.status_code, 404)
            
    def test_already_answer(self):
         with self.client:
            self.post_answer()
            response = self.client.post('api/v1/answers', data=json.dumps(answer3_to_post),
                                        headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 404)
            
    def test_delete_answer(self):
        self.post_answer()
        
        response = self.client.delete('api/v1/answer/1', headers = {'content-type': 'application' '/json'})
        
        self.assertEqual(response.status_code, 200)
        
    def test_edit_answer(self):
        """Tests for editing a political party"""
        with self.client:
            self.post_question()
            response = self.client.post('api/v1/answer/1', data=json.dumps(answer1_to_post),
                                         headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response.status_code, 201)
            response = self.client.put('api/v1/answers/1', data=json.dumps(answer1_to_post),
                                         headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response.status_code, 201)
            
    def test_doc(self):
        with self.client:
            response = self.client.get('/', headers={'Content-Type': 'application' '/json'})
            self.assertEqual(response._status_code, 404)
            
    def test_answer_with_no_description(self):
         with self.client:
             response1 = self.post_question()
            
             
             response = self.client.post('api/v1/answer/1', data=json.dumps(answer4_to_post),
                                         headers = {'content-type': 'application' '/json'})
             self.assertEqual(response.status_code, 400)    