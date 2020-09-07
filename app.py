from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('weather.html')