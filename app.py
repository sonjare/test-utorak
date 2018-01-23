
from flask import Flask
from models import Comment

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome"

    
def view():
