#!/usr/bin/python
from collections import namedtuple
import json
import random

def load_exercises(filename="exercise.json"):
    with open(filename, 'r') as json_file:
        exercises = json.load(json_file)
    
    Exercise = namedtuple('Exercise','Name, Type, Reps')
    
    list_of_exercises=[]

    for exercise in exercises:
        list_of_exercises.append(Exercise(**exercise))

    return list_of_exercises

def pick_exercise(exercises,num=3):
    picked_exercise=[]
    while len(picked_exercise)<num:
        exercise = random.choice(exercises)
        exercises.remove(exercise)
        flag = False
        for i in picked_exercise:
            if exercise.Type == i.Type:
                flag = True
                break
        if flag == False:
            picked_exercise.append(exercise)
            exercise_print(exercise)
            # print(exercise.Name)
    
    return picked_exercise

def exercise_print(exercise):
    print("Name: {}".format(exercise.Name))
    print("Type: {}".format(exercise.Type))
    print("Reps: {}".format(random.randint(exercise.Reps[0],exercise.Reps[1])))
    print("\n")

