'''
Filename: /home/deniojr/Desktop/python_projects/fitness_app/api/app/schema.py
Path: /home/deniojr/Desktop/python_projects/fitness_app/api
Created Date: Friday, March 8th 2024, 11:05:23 am
Author: Dênio Barbosa Júnior

Copyright (c) 2024 Your Company
'''

from .db import get_db_connection, create_tables

conn = get_db_connection()
cursor = conn.cursor()
for create_tables in create_tables:
    cursor.execute(create_tables)
conn.commit()
cursor.close()
conn.close()
