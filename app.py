from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask app users, i just pushed my code to the github repo to trigger build'