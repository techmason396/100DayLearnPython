import os
students_scores = {
    "Harry": 81,
    "Ron": 78,
    "Herminone": 99,
    "Draco": 74,
    "Neville": 62,
}


for score in students_scores:
    print(students_scores[score])

os.system('cls' if os.name == 'nt' else 'clear')
