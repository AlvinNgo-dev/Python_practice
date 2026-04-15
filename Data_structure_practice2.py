def show_report(report):
    print("Student Score Report:")
    for student in report:
        print(student["name"], ":", student["score"])


def add_grade(report):
    name = input("Enter name: ")
    score = int(input("Enter score: "))
    report.append({"name": name, "score": score})
    print("Added successfully!")


def remove_grade(report):
    name = input("Enter name: ")
    for student in report:
        if student["name"] == name:
            report.remove(student)
            print("Removed successfully!")
            return
    print("Student not found.")


def average_score(report):
    total = 0
    count = 0
    for student in report:
        total += student["score"]
        count += 1
    print("Average score is:", round(total / count, 3))


report = [
    {"name": "Alvin", "score": 90},
    {"name": "Bella", "score": 85},
    {"name": "Chris", "score": 78},
    {"name": "Diana", "score": 92},
    {"name": "Ethan", "score": 88}
]

while True:
    print(
        "\nChoose an option:\n"
        "1. Show Student score report\n"
        "2. Add student grade\n"
        "3. Calculate average score\n"
        "4. Remove student grade\n"
    )
    num = int(input())
    if num == 1:
        show_report(report)
    elif num == 2:
        add_grade(report)
    elif num == 3:
        average_score(report)
    elif num == 4:
        remove_grade(report)
    else:
        break
