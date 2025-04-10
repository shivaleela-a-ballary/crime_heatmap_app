@crimes_bp.route('/api/crimes', methods=['GET'])
def get_crimes():
    print("Fetching crime data...")
    crimes = CrimeIncident.query.all()
    return jsonify([{
        'latitude': crime.latitude,
        'longitude': crime.longitude,
        'type': crime.type,
        'severity': crime.severity
    } for crime in crimes])
