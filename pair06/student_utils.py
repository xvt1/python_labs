import random

def generate_grades(count):
    grades = []
    for i in range(count):
        grades.append(random.randint(1, 12))
    return grades

def avarege_grade(grades):
    return sum(grades) / len(grades)

def get_level(average):
    if(average >= 10):
        return "Високий"
    elif(average >= 7 and average <= 9.99):
        return "достатній"
    elif(average >= 4 and average <= 6.99):
        return "середній"
    elif(average < 4):
        return "початковий"

