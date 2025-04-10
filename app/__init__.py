from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] =  os.environ.get('postgresql://postgres:XMb0Yth0O2upcv7Q@db.hgzurlphmpwvrsxowisx.supabase.co:5432/postgres')
    db.init_app(app)

    from .routes.crimes import crimes_bp
    app.register_blueprint(crimes_bp)

    return app