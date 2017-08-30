# API call, main script

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hi'

def new_entry():