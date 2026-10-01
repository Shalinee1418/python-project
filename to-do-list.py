def to_do_list():
    tasks = []  # Initialize an empty list to store tasks

    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            if tasks:
                print("Your tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks added yet.")

        elif choice == "2":
            task = input("Enter a task: ").strip()
            tasks.append(task)
            print(f"'{task}' has been added to the list.")

        elif choice == "3":
            if tasks:
                try:
                    task_num = int(input("Enter the task number to remove: "))
                    if 0 < task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1)
                        print(f"Task '{removed_task}' removed.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks to remove.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

# Call the function to start the program
to_do_list()
