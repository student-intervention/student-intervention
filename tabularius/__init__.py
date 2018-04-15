from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_avatar import Avatar

# application is created as an instance of Flask and we pass it __name__
# in order load resources correctly for our module
app = Flask(__name__)
app.config.from_object(Config)

# database setup
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# handle logins
login = LoginManager(app)
login.login_view = 'login'

# TODO: use flask-avatars to remove dependency on gravatar
# handle avatars
# avatar = Avatar(app)

# we place the import statement here to avoid circular imports.
from tabularius import routes, models
