tasks=[]
while True:
    print("Options:\n1.Add\n2.Remove\n3.Display\n4.exit")
    choice=input("Enter your choice(1-4): " ).strip()
    if choice=="1":
        task=input("Enter the task to be added:").strip()
        tasks.append(task)
        print("Task added")
    elif choice=="2":
        if not tasks:
            print("No tasks are present to delete")
        else:
            task=input("Enter the task to be deleted: ")
            if task in tasks:
                tasks.remove(task)
                print("task is deleted")
            else:
                print("task not found")
    elif choice=="3":
        if not tasks:
            print("No tasks added yet")
        else:
            print(tasks)
    elif choice=="4":
        print("Byee!")
        break
    else:
        print("Invalid choice!please choose from 1,2,3,4.")

