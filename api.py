# Previous imports remain...
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/paria"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class WaterLevelModel(db.Model):
    __tablename__ = 'water_level'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())
    doors = db.Column(db.Integer())

    def __init__(self, date, discharge, height):
        self.date = date
        self.discharge = discharge
        self.height = height

    def __repr__(self):
        return f"<WaterLevel {self.name}>"
