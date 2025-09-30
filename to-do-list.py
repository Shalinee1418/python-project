def to_do_list():
 task = {}

while true:
    print("\n To-Do-List Menu:")
    print("1. view Task")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("choose an option: ").strip()

    if choice == "1":
        print("Your tasks: ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        else:
            print("No tasks added yet. ")

     elif choice == "2":
        task = input("Enter a task: ").strip()
        tasks.append(task)
        print(f"{task} has been added to the list")

        elif choice == "3":
            task_num = int(input("Enter the task number to remove: "))
            if 0 < task <= len(tasks):
                remove_task = task.pop(task_num - 1)
                print(f"Task '{remove_task}' removed.")
            else:
                print("Invalid task number. ")    

         elif choice == "4":
            print("Goodbye!") 

            break

            else:
                print("Invalid option")
                
                      
    to-do-list()            
 