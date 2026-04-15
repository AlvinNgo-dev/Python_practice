import os
from datetime import datetime
import json

FILE_NAME = "tasks.txt"


def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_id, title, status, deadline = [x.strip()
                                                    for x in line.strip().split("|")]
                tasks[int(task_id)] = {"title": title,
                                       "status": status, "deadline": deadline}
    return tasks


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task in tasks.items():
            file.write(
                f"{task_id} | {task['title']} | {task['status']} | {task['deadline']}\n"
            )


def add_task(tasks):
    title = input("Enter task title: ")
    deadline_str = input("Enter deadline (HH:MM DD-MM-YYYY ): ")
    try:
        deadline = datetime.strptime(deadline_str, "%H:%M %d-%m-%Y")
    except ValueError:
        print("Invalid date format.")
        return
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title,
                      "status": "incomplete", "deadline": deadline_str}
    save_tasks(tasks)
    print(f"Task '{title}' added.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available")
    else:
        for task_id, task in tasks.items():
            print(
                f"[{task_id}] {task['title']} | {task['status']} | {task['deadline']}")


def mark_task_complete(tasks):
    try:
        view_tasks(tasks)
        task_id = int(input("\nEnter task ID to mark as complete: "))
    except ValueError:
        print("Invalid ID.")
        return

    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        save_tasks(tasks)
        print(f"Task '{tasks[task_id]['title']}' marked as complete.")
    else:
        print("Task ID not found.")


def delete_task(tasks):
    try:
        view_tasks(tasks)
        task_id = int(input("\nEnter task ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        save_tasks(tasks)
        print(f"Task '{deleted_task['title']}' deleted.")
    else:
        print("Task ID not found.")


def export_to_json(tasks):
    JSON_name = input("Enter JSON file name: ")
    with open(JSON_name, "w") as file:
        json.dump(tasks, file, indent=4)
    print(f"Task exported to {JSON_name}")


def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Export to JSON file")
        print("6. Exit")
        choice = input("Enter your choice: \n")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            export_to_json(tasks)
        elif choice == "6":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again")


if __name__ == "__main__":
    main()
