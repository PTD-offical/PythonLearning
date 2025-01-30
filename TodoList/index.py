Tasks = []

# ToDoList Functions

# Add Task
def AddTask():
    NewTask = input("Enter the task: ")
    Tasks.append(NewTask)
    print(f"Task '{NewTask}' added successfully!")

# Remove Task
def RemoveTask():
    ViewTasks()
    if not Tasks:
        return
    try:
        taskToDelete = int(input("Enter a task number to delete: "))
        if 1 <= taskToDelete <= len(Tasks):
            removed_task = Tasks.pop(taskToDelete - 1)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print(f"Task number {taskToDelete} is out of range!")
    except ValueError:
        print("Invalid input! Please enter a valid task number.")

# View Tasks
def ViewTasks():
    if not Tasks:
        print("No tasks found!")
    else:
        print("Tasks:")
        for index, task in enumerate(Tasks, start=1):
            print(f"{index}. {task}")

# Main Application
if __name__ == "__main__":
    print("Welcome, User!")
    # Loop for the app
    while True:
        print("\nWhat do you want to do?")
        print("---------------------------------")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. View all tasks")
        print("4. Exit")
        print("---------------------------------")
        choice = input("Enter your choice: ")

        if choice == "1":
            AddTask()
        elif choice == "2":
            RemoveTask()
        elif choice == "3":
            ViewTasks()
        elif choice == "4":
            print("Goodbye, User 👋👋")
            break
        else:
            print("Invalid input! Please choose a valid option.")
