'''
Filename: /home/deniojr/Desktop/python_projects/fitness_app/api/app/routes.py
Path: /home/deniojr/Desktop/python_projects/fitness_app/api/app
Created Date: Friday, March 8th 2024, 11:33:53 am
Author: Dênio Barbosa Júnior

Copyright (c) 2024 Your Company
'''


from flask import request, jsonify
from .db import get_db_connection

def configure_routes(app):

    @app.route('/')
    def index():
        return "Fitness API is up and running!"

    @app.route('/exercises', methods=['POST'])
    def add_exercise():
        data = request.json
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO exercises (name, muscle_group) VALUES (%s, %s)", (data['name'], data['muscle_group']))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'status': 'Exercise added'}), 201

    @app.route('/exercises/<muscle_group>', methods=['GET'])
    def get_exercises(muscle_group):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM exercises WHERE muscle_group = %s", (muscle_group,))
        exercises = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(exercises), 200
