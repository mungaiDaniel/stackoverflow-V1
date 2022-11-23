"""initializing the application"""
from flask import Flask

from app.questions.views import V1

app = Flask(__name__)
app.register_blueprint(V1)
