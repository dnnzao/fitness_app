# /*
#  * Filename: /home/deniojr/Desktop/python_projects/fitness_app/api/__init__.py
#  * Path: /home/deniojr/Desktop/python_projects/fitness_app/api
#  * Created Date: Friday, March 8th 2024, 11:24:57 am
#  * Author: Dênio Barbosa Júnior
#  * 
#  * Copyright (c) 2024 Your Company
#  */


from flask import Flask
from .routes import configure_routes
from .migrations.migrate import migrate_database

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    configure_routes(app)
    
    app.cli.add_command(migrate_database)

    return app


