import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("firebase/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'your-database-url'
})

def send_alert(message, lat, lng):
    ref = db.reference('alerts')
    ref.push({
        'message': message,
        'latitude': lat,
        'longitude': lng
    })