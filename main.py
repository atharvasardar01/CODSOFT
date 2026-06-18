tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter Task: ")

        tasks.append({
            "task": task,
            "done": False
        })

        print("Task Added!")

    elif choice == "2":

        if len(tasks) == 0:
            print("No Tasks Found")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start=1):
                status = "✓" if task["done"] else "✗"
                print(f"{i}. {task['task']} [{status}]")

    elif choice == "3":

        number = int(input("Task Number: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            print("Task Completed!")
        else:
            print("Invalid Number")

elif choice == "4":

    number = int(input("Task Number: "))

    if 1 <= number <= len(tasks):
        tasks.pop(number - 1)
        print("Task Deleted!")
    else:
        print("Invalid Number")

    elif choice == "5":
        print("Goodbye!")
        break