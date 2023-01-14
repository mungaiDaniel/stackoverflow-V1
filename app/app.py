"""initializing the application"""
from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from pathlib import Path

from app.questions.views import V1
from app.answers.view import version1

app = Flask(__name__)
CORS(app)
app.register_blueprint(V1)
app.register_blueprint(version1)
app.debug = True
BASE_PATH = Path(__file__).resolve().parent

@app.route('/static/swagger.json')
def send_static():
    return send_from_directory('static', 'swagger.json')

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggeriu_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "stackoverflow-v1"
    }
)
app.register_blueprint(swaggeriu_blueprint, url_prefix=SWAGGER_URL)
