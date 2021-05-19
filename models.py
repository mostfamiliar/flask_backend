from __main__ import app
from flask.ext.sqlalchemy import SQLAlchemy


class TrailModel(db.Model):
    __tablename__ = 'water_level'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    route = db.Column(JSON)

    def __init__(self, name, date, discharge, height):
        self.name = name
        self.route = date

    def __repr__(self):
        return f"<Trail {self.name}>"


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
