from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
  return 'Hello, World!'
@app.route('/Mword')
def hello_Mworld():
  return 'Hello, M World!'
