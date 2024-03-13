# /*
#  * Filename: /home/deniojr/Desktop/python_projects/fitness_app/api/__init__.py
#  * Path: /home/deniojr/Desktop/python_projects/fitness_app/api
#  * Created Date: Friday, March 8th 2024, 11:24:57 am
#  * Author: Dênio Barbosa Júnior
#  * 
#  * Copyright (c) 2024 Your Company
#  */


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Config')

    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_RECORD_QUERIES"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        from . import routes, models
        routes.configure_routes(app)

    return app
