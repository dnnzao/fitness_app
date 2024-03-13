# Filename: models.py
# Path: /home/deniojr/Desktop/python_projects/fitness_app/api/app
# Created Date: Friday, March 8th 2024, 11:32:24 am
# Author: Dênio Barbosa Júnior

# Copyright (c) 2024 Your Company

from . import db

class MuscleGroup(db.Model):
    __tablename__ = 'muscle_groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

class Exercise(db.Model):
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    muscle_group_id = db.Column(db.Integer, db.ForeignKey('muscle_groups.id'))
    muscle_group = db.relationship('MuscleGroup', back_populates="exercises")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.Text, nullable=False, server_default='')


MuscleGroup.exercises = db.relationship('Exercise', order_by=Exercise.id, back_populates="muscle_group")

class Chest(db.Model):
    __tablename__ = 'chest'
    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

class Back(db.Model):
    __tablename__ = 'back'
    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

class Triceps(db.Model):
    __tablename__ = 'triceps'
    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

class Biceps(db.Model):
    __tablename__ = 'biceps'
    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

class Quadriceps(db.Model):
    __tablename__ = 'quadriceps'
    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

class Posterior(db.Model):
    __tablename__ = 'posterior'
    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

class Calves(db.Model):
    __tablename__ = 'calves'
    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    exercises = db.relationship('Exercise', backref='user', lazy=True)
