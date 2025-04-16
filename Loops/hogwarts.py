# students = ["Herminoe", "Harry", "Ron"]

# print(students[0])
# print(students[1])
# print(students[2])

# students = ["Herminoe", "Harry", "Ron"]

# for student in students:
#     print(student)

# students = ["Herminoe", "Harry", "Ron"]

# for i in range(len(students)):
#     print(i + 1, students[i])

# students = ["Herminoe", "Harry", "Ron"]
# houses = ["Gryffindor","Gryffindor","Gryffindor", "Slytherin"]

# students = {
#     "Herminoe" : "Gryffindor", 
#     "Harry" : "Gryffindor", 
#     "Ron" : "Slytherin"
# }

# print(students["Herminoe"])
# print(students["Harry"])
# print(students["Ron"])

# students = {
#     "Herminoe" : "Gryffindor", 
#     "Harry" : "Gryffindor", 
#     "Ron" : "Slytherin"
# }

# for student in students:
#     print(student, students[student] , sep = " , ")

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ", ")
