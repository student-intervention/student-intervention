from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# application is created as an instance of Flask and we pass it __name__
# in order load resources correctly for our module
app = Flask(__name__)
app.config.from_object(Config)

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# we place the import statement here to avoid circular imports.
from app import routes, models
