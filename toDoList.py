toDoList = []

while True:

    print("========++-- TO DO LIST --++=========")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Task")
    print("4. Exit\n")

    choose = input("Choose Any Option: ")

    if choose == "1":
        task = input("Enter a task: ")
        toDoList.append(task)
        print("Task Added ","\U00012713")

    elif choose == "2":
        task = input("Remove a Task : ")
        toDoList.remove(task)
        print("Task Removed", "\U00012713")

    elif choose == "3":
        print("Your Task : ")
        for task in toDoList:
            print("\n", task)

    elif choose == "4":

        print("Exit")
        break


    else:
        print("Ivalid Input :( ")