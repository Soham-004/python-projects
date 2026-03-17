# ========================================
# DAY-5 PROJECT: TO-DO LIST MANAGER
# ========================================

import csv
import os

# -------------------------------
# Step 1: Task Class
# -------------------------------
class Task:
    def __init__(self, title, priority, due_date, status):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.status = status

# -------------------------------
# Step 2: File Handling
# -------------------------------
FILE_NAME = "tasks.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Priority", "Due Date", "Status"])
        print("Task file created successfully!")

def save_task_to_file(task):
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([task.title, task.priority, task.due_date, task.status])
    print(f"Task '{task.title}' saved successfully!")

def read_tasks_from_file():
    tasks_list = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                task_obj = Task(row['Title'], row['Priority'], row['Due Date'], row['Status'])
                tasks_list.append(task_obj)
    return tasks_list

# -------------------------------
# Step 3: Task Functions
# -------------------------------
def add_task():
    title = input("Enter task title: ")
    priority = input("Choose priority (H/M/L): ")
    due_date = input("Enter due date (dd/mm/yyyy): ")
    status = "Pending"  # default status
    new_task = Task(title, priority, due_date, status)
    save_task_to_file(new_task)

def mark_done(title_to_mark):
    tasks = read_tasks_from_file()
    found = False
    for task in tasks:
        if task.title.lower() == title_to_mark.lower():
            task.status = "Done"
            found = True
    if not found:
        print(f"No task found with title '{title_to_mark}'")
        return

    # Rewrite the CSV with updated tasks
    with open(FILE_NAME, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Priority", "Due Date", "Status"])
        for task in tasks:
            writer.writerow([task.title, task.priority, task.due_date, task.status])
    print(f"Task '{title_to_mark}' marked as Done!")

def view_tasks(sorted_by="priority"):
    tasks = read_tasks_from_file()
    if sorted_by == "priority":
        priority_order = {"H": 1, "M": 2, "L": 3}
        tasks.sort(key=lambda x: priority_order.get(x.priority.upper(), 4))
    elif sorted_by == "due_date":
        # Sort by dd/mm/yyyy
        tasks.sort(key=lambda x: tuple(map(int, x.due_date.split("/")[::-1])))  # yyyy, mm, dd

    print("\n----- TASK LIST -----")
    for task in tasks:
        print(f"Title: {task.title}, Priority: {task.priority}, Due: {task.due_date}, Status: {task.status}")
    print("--------------------")

# -------------------------------
# Step 4: Main Menu Loop
# -------------------------------
def main():
    initialize_file()  # ensure CSV exists

    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task()

        elif choice == "2":
            sort_choice = input("Sort tasks by Priority or Due Date? (P/D): ").upper()
            if sort_choice == "D":
                view_tasks(sorted_by="due_date")
            else:
                view_tasks(sorted_by="priority")

        elif choice == "3":
            title_to_mark = input("Enter the title of the task to mark as Done: ")
            mark_done(title_to_mark)

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-4.")

# Run the program
if __name__ == "__main__":
    main()