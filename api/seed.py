'''
Filename: /home/deniojr/Desktop/python_projects/fitness_app/api/seed.py
Path: /home/deniojr/Desktop/python_projects/fitness_app/api
Created Date: Monday, March 11th 2024, 10:22:20 am
Author: Dênio Barbosa Júnior

Copyright (c) 2024 Your Company
'''


import psycopg2
from psycopg2.extras import execute_values
from config import Config

def get_db_connection():
    return psycopg2.connect(Config.DATABASE_URI)

def seed_exercises():
    back_exercises = [
        "Pull-Ups",
        "Bent-Over Rows",
        "Deadlifts",
        "Lat Pulldowns",
        "T-Bar Rows",
        "Seated Cable Rows",
        "Face Pulls",
        "Single-Arm Dumbbell Rows",
        "Reverse Flyes",
        "Barbell Shrugs",
    ]
    chest_exercises = [
    "Barbell Bench Press",
    "Dumbbell Flyes",
    "Incline Bench Press",
    "Decline Bench Press",
    "Chest Dips",
    "Push-Ups",
    "Cable Flyes",
    "Pec Deck Machine",
    "Landmine Press",
    "Svend Press",
    ]

    triceps_exercises = [
        "Close-Grip Bench Press",
        "Tricep Dips",
        "Skull Crushers",
        "Overhead Tricep Extension",
        "Tricep Kickbacks",
        "Rope Pushdowns",
        "Diamond Push-Ups",
        "Single-Arm Tricep Extension",
        "Bench Dips",
        "Tricep Pushdown",
    ]

    biceps_exercises = [
        "Barbell Curls",
        "Dumbbell Curls",
        "Hammer Curls",
        "Preacher Curls",
        "Concentration Curls",
        "Cable Curls",
        "Zottman Curls",
        "Incline Dumbbell Curls",
        "Reverse Curls",
        "Spider Curls",
    ]

    quadriceps_exercises = [
        "Squats",
        "Leg Press",
        "Lunges",
        "Front Squats",
        "Hack Squats",
        "Leg Extensions",
        "Bulgarian Split Squats",
        "Goblet Squats",
        "Step-Ups",
        "Sissy Squats",
    ]

    posterior_leg_exercises = [
        "Romanian Deadlifts",
        "Leg Curls",
        "Good Mornings",
        "Stiff-Legged Deadlifts",
        "Back Extensions",
        "Glute-Ham Raises",
        "Reverse Hyperextensions",
        "Single-Leg Deadlifts",
        "Pull Throughs",
        "Nordic Hamstring Curls",
    ]


    conn = get_db_connection()
    cursor = conn.cursor()

    insert_query = "INSERT INTO Back (name) VALUES %s ON CONFLICT (name) DO UPDATE SET name = EXCLUDED.name"
    execute_values(cursor, insert_query, [(exercise,) for exercise in back_exercises], page_size=100)

    chest_insert_query = "INSERT INTO Chest (name) VALUES %s ON CONFLICT (name) DO UPDATE SET name = EXCLUDED.name"
    execute_values(cursor, chest_insert_query, [(exercise,) for exercise in chest_exercises], page_size=100)

    triceps_insert_query = "INSERT INTO Triceps (name) VALUES %s ON CONFLICT (name) DO UPDATE SET name = EXCLUDED.name"
    execute_values(cursor, triceps_insert_query, [(exercise,) for exercise in triceps_exercises], page_size=100)

    biceps_insert_query = "INSERT INTO Biceps (name) VALUES %s ON CONFLICT (name) DO UPDATE SET name = EXCLUDED.name"
    execute_values(cursor, biceps_insert_query, [(exercise,) for exercise in biceps_exercises], page_size=100)

    quadriceps_insert_query = "INSERT INTO Quadriceps (name) VALUES %s ON CONFLICT (name) DO UPDATE SET name = EXCLUDED.name"
    execute_values(cursor, quadriceps_insert_query, [(exercise,) for exercise in quadriceps_exercises], page_size=100)

    posterior_insert_query = "INSERT INTO Posterior (name) VALUES %s ON CONFLICT (name) DO UPDATE SET name = EXCLUDED.name"
    execute_values(cursor, posterior_insert_query, [(exercise,) for exercise in posterior_leg_exercises], page_size=100)

    conn.commit()

    cursor.close()
    conn.close()

if __name__ == '__main__':
    seed_exercises()
