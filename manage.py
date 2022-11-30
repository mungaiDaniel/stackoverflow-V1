
from flask_script import Manager, Server
from app.app import app
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

manager = Manager(app)

manager.add_command('server', Server)

if __name__ == '__main__':
    manager.run()  
