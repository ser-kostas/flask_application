from flask import Flask
from models import db
from routes import main_blueprint

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mssql+pyodbc://@DESKTOP-H11M6GN/validata?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Register the blueprint for routes
app.register_blueprint(main_blueprint)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
