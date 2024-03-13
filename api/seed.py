# Filename: seed.py
# Path: /home/deniojr/Desktop/python_projects/fitness_app/api
# Created Date: Monday, March 11th 2024, 10:22:20 am
# Author: Dênio Barbosa Júnior


from app import create_app
from app.models import db, Exercise, MuscleGroup

app = create_app()

def seed_exercises():
    muscle_groups = {
        "Back": [
            "Pull-Ups", "Bent-Over Rows", "Deadlifts", "Lat Pulldowns",
            "T-Bar Rows", "Seated Cable Rows", "Face Pulls", "Single-Arm Dumbbell Rows",
            "Reverse Flyes", "Barbell Shrugs"
        ],
        "Chest": [
            "Barbell Bench Press", "Dumbbell Flyes", "Incline Bench Press",
            "Decline Bench Press", "Chest Dips", "Push-Ups", "Cable Flyes",
            "Pec Deck Machine", "Landmine Press", "Svend Press"
        ],
        "Biceps": [
            "Barbell Curls", "Dumbbell Curls", "Hammer Curls", "Preacher Curls",
            "Concentration Curls", "Cable Curls", "Zottman Curls", "Incline Dumbbell Curls",
            "Reverse Curls", "Spider Curls"
        ],
        "Triceps": [
            "Close-Grip Bench Press", "Tricep Dips", "Skull Crushers",
            "Overhead Tricep Extension", "Tricep Kickbacks", "Rope Pushdowns",
            "Diamond Push-Ups", "Single-Arm Tricep Extension", "Bench Dips",
            "Tricep Pushdown"
        ],
        "Quadriceps": [
            "Squats", "Leg Press", "Lunges", "Front Squats", "Hack Squats",
            "Leg Extensions", "Bulgarian Split Squats", "Goblet Squats", "Step-Ups",
            "Sissy Squats"
        ],
        "Posterior": [
            "Romanian Deadlifts", "Leg Curls", "Good Mornings", "Stiff-Legged Deadlifts",
            "Back Extensions", "Glute-Ham Raises", "Reverse Hyperextensions",
            "Single-Leg Deadlifts", "Pull Throughs", "Nordic Hamstring Curls"
        ]
    }

    for group_name, exercises in muscle_groups.items():
        muscle_group = MuscleGroup.query.filter_by(name=group_name).first()
        if not muscle_group:
            muscle_group = MuscleGroup(name=group_name)
            db.session.add(muscle_group)
            db.session.commit()

        for exercise_name in exercises:
            existing_exercise = Exercise.query.filter_by(name=exercise_name, muscle_group=muscle_group).first()
            if not existing_exercise:
                new_exercise = Exercise(name=exercise_name, muscle_group=muscle_group)
                db.session.add(new_exercise)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        seed_exercises()

