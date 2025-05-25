# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 13:19:49 2025

@author: Olkae
"""

import random

# Generate a list of workers
workers = []
for i in range(500):
    workers.append({
        "id": i + 1,
        "name": f"Worker_{i+1}",
        "salary": random.randint(4000, 40000),
        "gender": random.choice(["Male", "Female"])
    })

# Generate payment slips
for worker in workers:
    try:
        salary = worker["salary"]
        gender = worker["gender"]

        # Assign employee level
        if 10000 < salary < 20000:
            level = "A1"
        elif 7500 < salary < 30000 and gender == "Female":
            level = "A5-F"
        else:
            level = "B2"

        # Print payment slip
        print(f"ID: {worker['id']}, Name: {worker['name']}, Salary: ${salary}, Gender: {gender}, Level: {level}")

    except Exception as e:
        print(f"Error processing worker {worker['id']}: {e}")
