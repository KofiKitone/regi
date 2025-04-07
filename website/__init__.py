from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, makedirs
from flask_login import LoginManager
from models import db  

DB_NAME = "shoplift.db"

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config['SECRET_KEY'] = 'JAMESBONDISTHEBEST'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path.join(app.instance_path, DB_NAME)}'

    db.init_app(app)

    # Import models BEFORE creating the database
    # from models import User, Facility, Category, Booking  # Adjusted import to use absolute path

    create_database(app)  # Create database after models are imported

    from .routes import routes
    app.register_blueprint(routes, url_prefix='/')

    # login_manager = LoginManager()
    # login_manager.login_view = "auth.login"
    # login_manager.init_app(app)

    # @login_manager.user_loader
    # def load_user(id):
    #     return User.query.get(int(id))

    return app

def create_database(app):
    with app.app_context():  # Push the application context
        try:
            # Ensure the instance folder exists
            makedirs(app.instance_path, exist_ok=True)
        except Exception as e:
            print(f"Error creating instance folder: {e}")

        db_path = path.join(app.instance_path, DB_NAME)
        
        if not path.exists(db_path):
            db.create_all()
            print('Created Database')