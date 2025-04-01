from services.todolist import ToDoList

def print_menu():
    print("\nTo-Do List Management System:")
    print("1. Add a new task")
    print("2. Remove a task")
    print("3. Show all tasks")
    print("4. Save tasks")
    print("5. Exit")

def main():
    todo_list = ToDoList()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Task name: ")
            description = input("Task description: ")
            priority = input("Task priority (High/Medium/Low): ")
            todo_list.add_task(name, description, priority)
        elif choice == '2':
            name = input("Task name to remove: ")
            todo_list.remove_task(name)
        elif choice == '3':
            print("\nYour To-Do List:")
            todo_list.show_tasks()
        elif choice == '4':
            todo_list.save_tasks()
        elif choice == '5':
            print("Exiting...")
            todo_list.save_tasks()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
