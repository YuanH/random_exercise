#!/usr/bin/python
from collections import namedtuple
import json
import random
import datetime

def load_exercises(filename="exercise.json"):
    with open(filename, 'r') as json_file:
        exercises = json.load(json_file)
    
    Exercise = namedtuple('Exercise','Name, Type, Reps, Sets')
    
    list_of_exercises=[]

    for exercise in exercises:
        list_of_exercises.append(Exercise(**exercise))

    return list_of_exercises

def pick_exercise(exercises, sets=12):
    filename = "logs/" + datetime.datetime.now().strftime("%m-%d-%Y") + ".txt"
    f = open(filename, 'w')
    f.write(datetime.datetime.now().strftime("%a, %b %d, %Y %H:%M:%S"))
    f.write("\n")
    registered_types = []
    while sets > 0:
        exercise = random.choice(exercises)
        exercises.remove(exercise)
        flag = False

        # Check we already have an exercise that works the same muscle group
        for i in registered_types:
            if i in exercise.Type:
                flag = True
                break
        if flag == False:
            registered_types += exercise.Type
            if sets <= exercise.Sets[0]:
                temp_sets = exercise.Sets[0]
            else:
                temp_sets = random.randint(exercise.Sets[0],exercise.Sets[1])
            sets -= temp_sets
            temp_reps = random.randint(exercise.Reps[0],exercise.Reps[1])
            exercise_print(exercise, temp_reps, temp_sets, f)
            # print(exercise.Name)
    f.close()
    

def exercise_print(exercise, reps, sets, f):
    print("Name: {}".format(exercise.Name))
    f.write("Name: {}\n".format(exercise.Name))
    
    print("Type: " + ", ".join(exercise.Type))
    f.write("Type: " + ", ".join(exercise.Type))
    f.write("\n")
    
    print("Reps: {}".format(reps))
    f.write("Reps: {}\n".format(reps))

    print("Sets: {}".format(sets))
    f.write("Sets: {}\n".format(sets))
    print("\n")
    f.write("\n")

