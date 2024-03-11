'''
Filename: /home/deniojr/Desktop/python_projects/fitness_app/api/app/db.py
Path: /home/deniojr/Desktop/python_projects/fitness_app/api/app
Created Date: Friday, March 8th 2024, 11:32:29 am
Author: Dênio Barbosa Júnior

Copyright (c) 2024 Your Company
'''

import psycopg2
from config import Config

def get_db_connection():
    return psycopg2.connect(Config.DATABASE_URI)

def drop_tables():
    commands = [
        "DROP TABLE IF EXISTS Exercises;",
        "DROP TABLE IF EXISTS Posterior;",
        "DROP TABLE IF EXISTS Quadriceps;",
        "DROP TABLE IF EXISTS Triceps;",
        "DROP TABLE IF EXISTS Biceps;",
        "DROP TABLE IF EXISTS Back;",
        "DROP TABLE IF EXISTS Chest;",
    ]
    conn = get_db_connection()
    cursor = conn.cursor()
    for command in commands:
        cursor.execute(command)
    conn.commit()
    cursor.close()
    conn.close()

def create_tables():
    commands = [
        """
        CREATE TABLE IF NOT EXISTS Chest (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL UNIQUE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Back (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL UNIQUE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Biceps (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL UNIQUE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Triceps (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL UNIQUE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Quadriceps (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL UNIQUE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Posterior (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL UNIQUE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Exercises (
            id SERIAL PRIMARY KEY,
            chest_id INT,
            back_id INT,
            biceps_id INT,
            triceps_id INT,
            quadriceps_id INT,
            posterior_id INT,
            FOREIGN KEY (chest_id) REFERENCES Chest(id),
            FOREIGN KEY (back_id) REFERENCES Back(id),
            FOREIGN KEY (biceps_id) REFERENCES Biceps(id),
            FOREIGN KEY (triceps_id) REFERENCES Triceps(id),
            FOREIGN KEY (quadriceps_id) REFERENCES Quadriceps(id),
            FOREIGN KEY (posterior_id) REFERENCES Posterior(id)
        );
        """
    ]
    conn = get_db_connection()
    cursor = conn.cursor()
    for command in commands:
        cursor.execute(command)
    conn.commit()
    cursor.close()
    conn.close()

def main():
    drop_tables()
    create_tables()

if __name__ == "__main__":
    main()