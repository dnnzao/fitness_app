'''
Filename: /home/deniojr/Desktop/python_projects/fitness_app/api/app/routes.py
Path: /home/deniojr/Desktop/python_projects/fitness_app/api/app
Created Date: Friday, March 8th 2024, 11:33:53 am
Author: Dênio Barbosa Júnior

Copyright (c) 2024 Your Company
'''


from flask import Flask, jsonify
from . import db
from .models import Exercise, MuscleGroup

def configure_routes(app):

    # GET methods
    @app.route('/exercises', methods=['GET'])
    def get_all_exercises():
        exercises = Exercise.query.all()
        return jsonify([{'id': exercise.id, 'name': exercise.name, 'description': exercise.description, 'muscle_group': exercise.muscle_group.name} for exercise in exercises])

    @app.route('/exercises/<muscle_group>', methods=['GET'])
    def get_exercises_by_muscle_group(muscle_group):
        muscle_group_model = MuscleGroup.query.filter(MuscleGroup.name.ilike(muscle_group)).first()
        if muscle_group_model:
            exercises = Exercise.query.filter_by(muscle_group_id=muscle_group_model.id).all()
            return jsonify([{'id': exercise.id, 'name': exercise.name, 'description': exercise.description} for exercise in exercises])
        return jsonify(error='Invalid muscle group name'), 404

    @app.route('/exercises/<muscle_group>/<int:id>', methods=['GET'])
    def get_exercise_by_id(muscle_group, id):
        muscle_group_model = MuscleGroup.query.filter_by(name=muscle_group.capitalize()).first()
        if muscle_group_model:
            exercise = Exercise.query.filter_by(id=id, muscle_group_id=muscle_group_model.id).first()
            if exercise:
                return jsonify({'id': exercise.id, 'name': exercise.name, 'description': exercise.description})
            return jsonify(error='Exercise not found'), 404
        return jsonify(error='Invalid muscle group name'), 404
    
    # POST methods
    @app.route('/exercise', methods=['POST'])
    def add_exercise():
        data = request.get_json()
        muscle_group = MuscleGroup.query.get(data.get('muscle_group_id'))
        if not muscle_group:
            return jsonify(error="Muscle group not found"), 404
        new_exercise = Exercise(name=data.get('name'), muscle_group=muscle_group)
        db.session.add(new_exercise)
        db.session.commit()
        return jsonify({"id": new_exercise.id, "name": new_exercise.name, "muscle_group": muscle_group.name}), 201

    # PUT methods
    @app.route('/exercise/<int:id>', methods=['PUT'])
    def update_exercise(id):
        exercise = Exercise.query.get(id)
        if not exercise:
            return jsonify(error='Exercise not found'), 404

        data = request.get_json()
        exercise.name = data.get('name', exercise.name)
        muscle_group_id = data.get('muscle_group_id')
        if muscle_group_id:
            muscle_group = MuscleGroup.query.get(muscle_group_id)
            if not muscle_group:
                return jsonify(error="Muscle group not found"), 404
            exercise.muscle_group = muscle_group
        
        db.session.commit()
        return jsonify({'id': exercise.id, 'name': exercise.name, 'muscle_group': exercise.muscle_group.name})

    # DELETE methods
    @app.route('/exercise/<int:id>', methods=['DELETE'])
    def delete_exercise(id):
        exercise = Exercise.query.get(id)
        if not exercise:
            return jsonify(error='Exercise not found'), 404

        db.session.delete(exercise)
        db.session.commit()
        return jsonify({'message': 'Exercise deleted'})

    
