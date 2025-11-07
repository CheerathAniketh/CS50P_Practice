students = [
    {"name": "hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", 'house': 'Gryffindor', 'patronus': "jack russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}

]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
