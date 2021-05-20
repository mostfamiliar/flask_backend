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
    date= db.Column(db.DateTime())
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


@app.route('/water_levels', methods=['GET'])
def handle_water_levels():
    if request.method == 'GET':
        month = request.args.get('month')

        water_level = WaterLevelModel.query.with_entities(func.avg(WaterLevelModel.height)).filter(extract('month', WaterLevelModel.date)==str(month)).all()

        result = [round(r,1) for r, in water_level]

        return jsonify({"water_level": result[0]})
