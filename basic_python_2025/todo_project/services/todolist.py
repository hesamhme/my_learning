from models.task import Task
import csv
import os

class ToDoList:
    def __init__(self, file_path='data/tasks.csv'):
        self.tasks = []
        self.file_path = file_path
        self.load_tasks()

    def add_task(self, name, description, priority):
        task = Task(name, description, priority)
        self.tasks.append(task)
        print(f"Task '{name}' added successfully!")

    def remove_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                print(f"Task '{name}' removed successfully!")
                return
        print(f"No task found with name '{name}'.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for task in self.tasks:
            print(task)

    def save_tasks(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Description', 'Priority'])
            writer.writeheader()
            for task in self.tasks:
                writer.writerow(task.to_dict())
        print("Tasks saved successfully!")

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.tasks = [Task.from_dict(row) for row in reader]
            print("Tasks loaded successfully!")
        else:
            print("No saved tasks found.")
