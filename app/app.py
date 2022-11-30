"""initializing the application"""
from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

from app.questions.views import V1
from app.answers.view import version1

app = Flask(__name__)
app.register_blueprint(V1)
app.register_blueprint(version1)
app.debug = True

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

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
