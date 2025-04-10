from flask import Blueprint, jsonify
from ..models.crime import CrimeIncident

crimes_bp = Blueprint('crimes', __name__)

@crimes_bp.route('/api/crimes', methods=['GET'])
def get_crimes():
    crimes = CrimeIncident.query.all()
    return jsonify([{
        'latitude': crime.latitude,
        'longitude': crime.longitude,
        'type': crime.type,
        'severity': crime.severity
    } for crime in crimes])