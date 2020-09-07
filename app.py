from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'

db = SQLAlchemy(app)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    cities = City.query.all()

    apikey = '7346aed032efee7291d5370de0809643'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'

    weather_data = []

    for city in cities: 

        r = requests.get(url.format(city.name,apikey)).json()
        print(r)

        weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'icon': r['weather'][0]['icon'],
            'description': r['weather'][0]['description'],
        }

    weather_data.append(weather)
    return render_template('weather.html', weather_data=weather_data)

