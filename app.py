from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
  return 'Hello, World!'
@app.route('/palmword')
def hello_world():
  return 'Hello, M World!'
