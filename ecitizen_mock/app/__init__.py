from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()
import os
base_dir = os.path.abspath(os.path.dirname(__file__))
template_path = os.path.join(base_dir, '..', 'templates')

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

def create_app():

    app = Flask(__name__)

    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    login_manager.login_view = "auth.login"

    from app.routes.main import bp
    from app.routes.auth import auth

    app.register_blueprint(bp)
    app.register_blueprint(auth)

    return app