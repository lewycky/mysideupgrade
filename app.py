from flask import Flask


app = Flask(__name__)


@app.route('/home')
def index():
    return '<h1>Manchester United 3-1 Arsenal</h2>'
    