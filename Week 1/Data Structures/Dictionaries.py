student = {"name": "Alice", "age": 25, "grade": "A"}

student["subject"] = "Math"
student["age"] = 32

# print(student)

# del student["grade"]

# print(student)

# student.pop("subject")

# print(student)

for key, value in student.items():
    print(key, value)
