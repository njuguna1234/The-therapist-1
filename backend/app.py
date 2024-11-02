from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from routes import setup_routes

app = Flask(__name__)
CORS(app)

# Configure database URI (Render automatically sets the DATABASE_URL environment variable)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Use 'sqlite:///app.db' for local development
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

setup_routes(app, db)

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
