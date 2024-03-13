# Filename: seed.py
# Path: /home/deniojr/Desktop/python_projects/fitness_app/api
# Created Date: Monday, March 11th 2024, 10:22:20 am
# Author: Dênio Barbosa Júnior


# Filename: seed.py
# Path: /home/deniojr/Desktop/python_projects/fitness_app/api
# Updated to seed exercises with descriptions


from app import create_app
from app.models import db, Exercise, MuscleGroup

app = create_app()

def seed_exercises():
    exercise_descriptions = {
        "Back": {
            "Pull-Ups": "Targets latissimus dorsi, biceps, and forearms. Hang from a pull-up bar with an overhand grip, pull your body up until your chin clears the bar, then lower yourself back down in a controlled manner. Keep your core engaged and avoid swinging to maintain proper form. Focus on squeezing your back muscles at the top of the movement.",
            "Bent-Over Rows": "Primarily works the latissimus dorsi, rhomboids, and middle trapezius. Bend at the hips, keep your back straight, and pull the weight towards your lower ribcage, then slowly lower it back. Keep your elbows close to your body and maintain a slight bend in your knees throughout. Ensure your back is parallel to the ground for effective targeting.",
            "Deadlifts": "Engages the lower back, glutes, hamstrings, and traps. Stand with feet hip-width apart, grip the barbell with hands just outside your legs, lift by pushing through your heels and straightening your legs, then lower the bar back to the ground. Keep your back straight and core engaged to protect your spine. Drive the movement from your hips and legs.",
            "Lat Pulldowns": "Targets the latissimus dorsi, biceps, and rear deltoids. Sit at a pulldown machine, grasp the bar with a wide grip, pull the bar down to chest level while squeezing your shoulder blades together, then slowly return to the starting position. Ensure your movements are controlled, focusing on using your back muscles to perform the work. Avoid leaning too far back.",
            "T-Bar Rows": "Focuses on the middle and upper back, particularly the latissimus dorsi, rhomboids, and traps. Stand over the T-bar row machine, bend your knees slightly and lean forward, grasp the handles and pull the weight towards your chest, then lower it back down. Keep your back straight and avoid jerking motions. Ensure you pull with your back muscles, not your arms.",
            "Seated Cable Rows": "Works the latissimus dorsi, rhomboids, and lower trapezius. Sit on the machine, feet braced, grasp the cable handle, pull towards your waist while keeping your back straight, then return the handle slowly. Keep your movements smooth and controlled, focusing on squeezing your back muscles. Avoid rounding your back or using momentum.",
            "Face Pulls": "Targets the rear deltoids, traps, and upper back. Attach a rope to a cable machine at upper chest level, pull the rope towards your face while keeping your upper arms parallel to the ground, then slowly return to starting position. Keep your elbows high and squeeze your shoulder blades together. Ensure constant tension in the cable.",
            "Single-Arm Dumbbell Rows": "Engages the latissimus dorsi, biceps, and shoulders. Place one knee and hand on a bench, lift a dumbbell with the other hand in a rowing motion towards your hip, then lower it back down. Keep your back flat and avoid twisting your torso. Pull the weight with your back muscles, not just your arm.",
            "Reverse Flyes": "Targets the rear deltoids, upper back, and traps. Bend forward at the hips, hold dumbbells with palms facing each other, lift arms to the sides until parallel to the floor, then lower them again. Keep a slight bend in your elbows throughout the movement. Focus on using your rear deltoids to lift the weights.",
            "Barbell Shrugs": "Isolates the trapezius muscles. Stand upright, hold a barbell in front of you, lift your shoulders straight up towards your ears, and then lower them back down. Keep your arms straight and avoid rolling your shoulders. Focus on the upward lift and a controlled descent."
        },
        "Chest": {
            "Barbell Bench Press": "Targets the pectoralis major, anterior deltoids, and triceps. Lie back on a bench, grip the barbell with hands slightly wider than shoulder-width, lower it to your mid-chest, then press it upwards until your arms are fully extended. Keep your feet flat on the ground and maintain a slight arch in your lower back. Focus on moving the weight with your chest muscles.",
            "Dumbbell Flyes": "Isolates the pectoralis major while also engaging the deltoids. Lie on a bench with a dumbbell in each hand, extend your arms above your chest with a slight bend at the elbows, lower the weights in a wide arc until you feel a stretch in your chest, then bring them back together. Keep the movement controlled and focus on using your chest to pull the weights.",
            "Incline Bench Press": "Targets the upper pectoralis major and anterior deltoids. Set the bench to a 30-45 degree incline, grip the bar with hands just wider than shoulder-width, lower it to the upper part of your chest, then press it upwards until your arms are extended. Maintain control of the barbell and avoid arching your back excessively.",
            "Decline Bench Press": "Focuses on the lower pectoralis major. Secure your legs at the end of the decline bench, grip the barbell with hands wider than shoulder-width, lower it to the bottom of your chest, then press it upwards until your arms are fully extended. Keep the motion smooth and ensure you're pushing with your chest.",
            "Chest Dips": "Primarily targets the lower pectoralis major and triceps. Use parallel bars, lean forward slightly, lower your body until your shoulders are below your elbows, then push yourself back up to the starting position. Keep your elbows close to your body and avoid swinging.",
            "Push-Ups": "Engages the pectoralis major, triceps, and anterior deltoids. Place your hands slightly wider than shoulder-width apart on the ground, lower your body until your chest nearly touches the floor, then push back up to the starting position. Keep your body straight and tighten your core throughout the movement.",
            "Cable Flyes": "Targets the pectoralis major while involving the deltoids and biceps. Stand between two cable towers, grasp the handles, step forward and bring your hands together in a wide arc with a slight bend in your elbows, then slowly return to the starting position. Keep your chest up and focus on squeezing your pecs.",
            "Pec Deck Machine": "Isolates the pectoralis major. Sit on the machine with your back flat against the pad, place your arms on the pads, and bring them together in front of you, then slowly return to the starting position. Ensure that you're using your chest muscles to initiate the movement.",
            "Landmine Press": "Primarily works the upper pectoralis major and shoulders. Stand holding the end of a barbell secured in a landmine attachment, press the barbell upwards and slightly out, then bring it back down to chest level. Keep your core tight and maintain a slight bend in your knees throughout.",
            "Svend Press": "Isolates the pectoralis major, particularly the inner chest. Hold a weight plate between your palms at chest level, press the plate straight out in front of you until your arms are extended, then slowly bring it back in. Focus on squeezing your chest throughout the movement."
        },
        "Biceps": {
            "Barbell Curls": "Targets the biceps brachii. Stand with feet shoulder-width apart, hold a barbell at hip level, curl the weight towards your shoulders while keeping your elbows close to your torso, then lower back down with control. Ensure your upper arms remain stationary throughout the exercise.",
            "Dumbbell Curls": "Focuses on the biceps brachii and allows for individual arm training. Hold a dumbbell in each hand at arm's length, curl one weight while rotating your forearm so your palm faces your shoulder at the top, then lower back down and repeat with the other arm. Keep your elbows close to your sides and avoid swinging the weights.",
            "Hammer Curls": "Target both the biceps brachii and the brachialis. With a dumbbell in each hand, palms facing your torso, lift the weight by bending your elbow and keep your palm facing inwards throughout; then lower slowly. Maintain a stable posture, avoiding any swinging or excessive body movement.",
            "Preacher Curls": "Isolate the biceps by preventing shoulder movement. Sit at a preacher bench, rest your upper arms on the pad, curl the weight from the fully extended arm position up to your shoulders, and then lower it back down under control. Keep your shoulders and body still throughout.",
            "Concentration Curls": "Specifically target the biceps brachii for peak contraction. Sit with legs spread, elbow on the inside of your thigh, curl a dumbbell from this position up to your chest, then lower under control. Keep your upper body still and focus on isolating the bicep.",
            "Cable Curls": "Provide constant tension to the biceps. Stand in front of a cable machine, grab the bar attachment, curl the bar towards your shoulders while keeping your elbows fixed and down, then slowly extend your arms back to the starting position. Ensure a full range of motion for maximum effectiveness.",
            "Zottman Curls": "Work both the biceps and forearms. Curl dumbbells with palms facing up, at the top of the movement, rotate your hands so palms face down, then lower the weights. Reverse the grip again at the bottom of the movement. Maintain controlled movements throughout.",
            "Incline Dumbbell Curls": "Target the biceps with an emphasis on the lower part of the muscle. Lie back on an incline bench, let your arms hang down, curl the weights up, then lower them back down. Keep your shoulders back and avoid lifting your elbows.",
            "Reverse Curls": "Strengthen the biceps and the forearm extensors. Hold a barbell or dumbbells with an overhand grip, keep your wrists straight, curl the weights towards your shoulders, then lower them back down slowly. Keep your elbows close to your body throughout the movement.",
            "Spider Curls": "Isolate the biceps by preventing body momentum. Lie prone on an incline bench, let your arms hang straight down, curl the weight up towards your shoulders, and then lower under control. Ensure that your upper body remains still throughout the exercise."
        },
        "Triceps": {
            "Close-Grip Bench Press": "Primarily targets the triceps brachii alongside the chest and shoulders. Lie on a bench, grip the barbell with hands closer than shoulder-width, lower it to your chest while keeping your elbows close to your body, then press up to full arm extension.",
            "Tricep Dips": "Focus on the triceps, also engaging the chest and shoulders. Using parallel bars or a bench, lower your body with arms straight and elbows close to your body, then push back up to the starting position, focusing on using your triceps.",
            "Skull Crushers": "Isolate the triceps. Lie on a bench, extend arms upward holding a barbell or dumbbells, bend your elbows to lower the weight towards your forehead, then extend your arms to return to the starting position, keeping your upper arms stationary.",
            "Overhead Tricep Extension": "Targets the triceps, emphasizing the long head. Hold a dumbbell or barbell overhead, bend your elbows to lower the weight behind your head, then extend your arms to lift the weight back up, keeping your elbows pointed upwards.",
            "Tricep Kickbacks": "Isolate the triceps with a focus on the contraction. Lean forward with a dumbbell in hand, keep your elbow close to your body and at a 90-degree angle, then extend your arm to push the weight back, and finally return to the starting position.",
            "Rope Pushdowns": "Targets the triceps muscles. Stand facing a cable machine with a rope attachment, grasp the rope with both hands, push down by extending your arms fully, focusing on contracting the triceps, then slowly return to the starting position.",
            "Diamond Push-Ups": "Focuses on the triceps, chest, and shoulders. Place your hands close together on the floor, forming a diamond shape with your thumbs and index fingers, lower your body down keeping your elbows close to your sides, then push back up to the start.",
            "Single-Arm Tricep Extension": "Isolates the triceps. Stand or sit with a dumbbell in one hand, raise your arm above your head, bend your elbow to lower the dumbbell behind your head, then extend your arm to return to the start, focusing on the triceps.",
            "Bench Dips": "Primarily target the triceps, also engaging the shoulders and chest. Place your hands on a bench behind you, extend your legs out, lower your body by bending your elbows, then press up to return to the starting position.",
            "Tricep Pushdown": "Works the triceps muscles. Stand in front of a cable machine, grab the bar or handle attached to the high pulley, push down until your arms are fully extended, then slowly release back to the starting position."
        },
        "Quadriceps": {
            "Squats": "Engage the quadriceps, glutes, and lower back. Stand with feet shoulder-width apart, bend your knees to lower your body as if sitting back into a chair, keeping your chest up and knees over your toes, then return to standing.",
            "Leg Press": "Specifically targets the quadriceps, glutes, and hamstrings. Sit in a leg press machine, place your feet shoulder-width apart on the platform, extend your legs to push the weight, then slowly return to the starting position.",
            "Lunges": "Work the quadriceps, glutes, and hamstrings. Step forward with one leg, lower your hips to drop your back knee towards the floor, keep your front knee over the ankle, then push back to the starting position and repeat with the other leg.",
            "Front Squats": "Focus on the quadriceps and core. Hold a barbell at your chest with elbows up, perform a squat by lowering your body, keeping your back straight and elbows high, then drive back up to the starting position.",
            "Leg Extensions": "Isolate the quadriceps. Sit on a leg extension machine, adjust the pad to fit your legs, extend your knees to lift the weight, then slowly lower back to the starting position.",
            "Hack Squats": "Target the quadriceps, glutes, and calves. Stand in a hack squat machine, place your shoulders under the pads, squat down while keeping your back against the pad, then drive up to the starting position.",
            "Bulgarian Split Squats": "Focus on quadriceps and glutes. Stand lunge-length in front of a bench, elevate your rear foot on the bench, lower into a lunge, keeping your front knee aligned with your toe, then drive back up.",
            "Goblet Squats": "Engage quadriceps, glutes, and core. Hold a kettlebell or dumbbell close to your chest, squat down keeping your back straight and elbows between your knees, then return to the start, keeping your weight on your heels.",
            "Step-Ups": "Target the quadriceps, glutes, and hamstrings. Stand in front of a bench or step, step up with one leg, bringing the opposite knee up, then step down and repeat with the other leg, keeping your movements controlled.",
            "Sissy Squats": "Isolate the quadriceps. Stand with your feet hip-width apart, lean back as you slowly bend your knees and slide down an imaginary wall, then raise back up to the starting position, keeping tension on the quads."
        },
        "Posterior": {
            "Romanian Deadlifts": "Target the hamstrings, glutes, and lower back. Hold a barbell in front of you, hinge at your hips to lower the bar while keeping your back straight, then return to the upright position.",
            "Leg Curls": "Isolate the hamstrings. Lie face down on a leg curl machine, hook your ankles under the padded bar, curl your legs towards your buttocks, then slowly return to the starting position.",
            "Good Mornings": "Strengthen the lower back, glutes, and hamstrings. Stand with your feet shoulder-width apart, place a barbell across your shoulders, bend forward at your hips while keeping your back straight, then return to the upright position.",
            "Stiff-Legged Deadlifts": "Emphasize the hamstrings and lower back. Hold a barbell or dumbbells, keep your legs straight but not locked, hinge at your hips to lower the weights, then return to the standing position, keeping your back flat.",
            "Back Extensions": "Focus on the lower back, also engaging the glutes and hamstrings. Position yourself in a back extension station, cross your arms over your chest, bend at the waist to lower your upper body, then lift back to the starting position.",
            "Glute-Ham Raises": "Target hamstrings, glutes, and lower back. Secure your ankles, lower your body forward while keeping your back straight, then use your hamstrings and glutes to pull back up to the starting position.",
            "Reverse Hyperextensions": "Focus on the lower back and glutes. Lie face down on a hyperextension bench, allow your legs to hang off the back, then lift your legs until they're parallel with the floor, then lower them back down slowly.",
            "Single-Leg Romanian Deadlifts": "Stabilize and strengthen the hamstrings and glutes. Hold a dumbbell in one hand, lift one leg off the ground behind you while hinging at your hips to lower the weight, then return to standing.",
            "Seated Leg Curls": "Isolate the hamstrings. Sit at a leg curl machine, adjust the pad to fit your legs, curl your legs towards your buttocks, then slowly return to the starting position.",
            "Pull-Throughs": "Engage the hamstrings, glutes, and lower back. Attach a rope to a cable machine, face away from the machine, grab the rope and step forward, hinge at your hips and pull the rope through your legs, then return to standing."
        },
        "Calves": {
            "Standing Calf Raises": "Target the gastrocnemius and soleus. Stand on a calf raise machine or edge of a step with heels hanging off, rise up onto your toes as high as possible, then lower back down below parallel.",
            "Seated Calf Raises": "Isolate the soleus. Sit on a calf raise machine, place your feet on the platform with your knees bent, lift the weight by rising onto your toes, then lower back down.",
            "Donkey Calf Raises": "Engage the gastrocnemius and soleus. Position yourself on a donkey calf raise machine or have a partner sit on your lower back, rise onto your toes as high as possible, then lower back down below parallel.",
            "Single-Leg Calf Raises": "Focus on balance and isolation of the calf muscles. Stand on one foot on a raised surface, such as a block or step, rise up onto your toes as high as possible, then lower back down below parallel.",
            "Calf Presses": "Target the gastrocnemius and soleus. Sit on a leg press machine, position your feet at the bottom of the platform, push the weight by extending your ankles, then return to the starting position.",
            "Barbell Calf Raises": "Strengthen the calf muscles. Stand with a barbell across your shoulders, rise up onto your toes as high as possible, then lower back down below parallel.",
            "Tibialis Raises": "Isolate the tibialis anterior. Sit on a bench with your feet hanging off, loop a resistance band around your toes and anchor the other end, dorsiflex your feet against the resistance, then return to the starting position.",
            "Calf Raises on Leg Press Machine": "Target the gastrocnemius and soleus. Sit on a leg press machine, position your feet at the bottom of the platform, push the weight by extending your ankles, then return to the starting position.",
            "Box Jumps": "Engage the calves for explosive power. Stand facing a box or platform, jump up onto the box, landing softly with bent knees, then step back down and repeat.",
            "Calf Raises on Smith Machine": "Target the gastrocnemius and soleus. Stand under a Smith machine bar, place your shoulders under the bar, rise up onto your toes as high as possible, then lower back down below parallel."
        }
    }

    for group_name, exercises in exercise_descriptions.items():
        muscle_group = MuscleGroup.query.filter_by(name=group_name).first()
        if not muscle_group:
            muscle_group = MuscleGroup(name=group_name)
            db.session.add(muscle_group)
            db.session.commit()

        for exercise_name, description in exercises.items():
            existing_exercise = Exercise.query.filter_by(name=exercise_name, muscle_group=muscle_group, description=description).first()
            if not existing_exercise:
                new_exercise = Exercise(name=exercise_name, muscle_group=muscle_group, description=description)
                db.session.add(new_exercise)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        seed_exercises()

