# Previous imports remain...
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import extract
from sqlalchemy.sql import func
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
from sqlalchemy.dialects.postgresql import JSON

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/paria"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class WaterLevelModel(db.Model):
    __tablename__ = 'water_level'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    date = db.Column(db.DateTime())
    discharge = db.Column(db.Float())
    height = db.Column(db.Float())

    def __init__(self, name, date, discharge, height):
        self.name = name
        self.date = date
        self.discharge = discharge
        self.height = height

    def __repr__(self):
        return f"<WaterLevel {self.name}>"

class TrailModel(db.Model):
    __tablename__ = 'trail'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    route = db.Column(JSON)

    def __init__(self, name, date, discharge, height):
        self.name = name
        self.route = date

    def __repr__(self):
        return f"<Trail {self.name}>"


class WeatherModel(db.Model):
    __tablename__ = 'weather'

    id = db.Column(db.Integer, primary_key=True)
    county = db.Column(db.String())
    temperature = db.Column(db.Float())
    date = db.Column(db.DateTime())

    def __init__(self, county, date, temperature):
        self.name = name
        self.date = date
        self.county = county
        self.temperature = temperature

    def __repr__(self):
        return f"<Weather {self.name}>"


@app.route('/streamflow', methods=['GET'])
def handle_water_levels():
    if request.method == 'GET':
        month = request.args.get('month')

        water_level = WaterLevelModel.query.with_entities(func.avg(WaterLevelModel.discharge)).filter(extract('month', WaterLevelModel.date)==str(month)).all()

        result = [round(r,1) for r, in water_level]

        return jsonify({"water_level": result[0]})


@app.route('/trail_routes', methods=['GET'])
def handle_trail_route():
    if request.method == 'GET':
        trail_routes = TrailModel.query.with_entities(TrailModel.route).all()

        result = [r for r, in trail_routes]

        return jsonify({"route": result[0]})


@app.route('/temperature', methods=['GET'])
def handle_temperature_route():
        month = request.args.get('month')

        temperature = WeatherModel.query.with_entities(WeatherModel.temperature).filter(extract('month', WaterLevelModel.date)==str(month)).all()

        result = [round(r,1) for r, in temperature]

        return jsonify({"temperature": result[0]})
