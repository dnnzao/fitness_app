'''
Filename: /home/deniojr/Desktop/python_projects/fitness_app/api/app/migrations/migrate.py
Path: /home/deniojr/Desktop/python_projects/fitness_app/api/app/migrations
Created Date: Friday, March 8th 2024, 12:30:43 pm
Author: Dênio Barbosa Júnior

Copyright (c) 2024 Your Company
'''


import click
from flask.cli import with_appcontext
from ..db import create_tables

@click.command('migrate')
@with_appcontext
def migrate_database():
    print("Starting database migration...")
    create_tables()
    print("Database migration completed successfully.")


if __name__ == "__main__":
    migrate_database()
