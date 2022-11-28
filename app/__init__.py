"""initializing the application"""
from flask import Flask

from app.questions.views import V1
from app.answers.view import version1

app = Flask(__name__)
app.register_blueprint(V1)
app.register_blueprint(version1)
app.debug = True

