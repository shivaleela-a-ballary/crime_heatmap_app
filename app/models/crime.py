from .. import db

class CrimeIncident(db.Model):
    __tablename__ = 'crime_incidents'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    severity = db.Column(db.String(20))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)