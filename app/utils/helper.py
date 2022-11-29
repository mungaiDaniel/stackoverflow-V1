import json
from functools import wraps

from flask import make_response, jsonify

question1_to_post = {
    "title": "Python",
    "description": "what is python"
}
question2_to_post = {
    "title": "Java",
    "description": "what is java"
}
question3_to_post = {
    "title": "SQL",
    "description": "what is SQL"
}

answer1_to_post = {
    "title": "python",
    "description": "python is programming language"
}
answer2_to_post = {
    "title": "java",
    "description": "object oriented programming"
}
answer3_to_post = {
    "title": "",
    "description": "standard query language"
}
answer4_to_post = {
    "title": "python",
    "decf": "name the datastructures in python"
}

question4_to_post = {
    "rt": "python",
    "descrption": "what is python"
}
question5_to_post = {
    "title": "python",
    "descion": "what is python"
}