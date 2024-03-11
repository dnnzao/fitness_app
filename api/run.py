'''
Filename: /home/deniojr/Desktop/python_projects/fitness_app/api/app/run.py
Path: /home/deniojr/Desktop/python_projects/fitness_app/api/app
Created Date: Friday, March 8th 2024, 11:35:00 am
Author: Dênio Barbosa Júnior

Copyright (c) 2024 Your Company
'''

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3003)
