
shopping_list = []

while True:

    print("\n ===========Shopping List=============")
    print("1. Add Items")
    print("2. Remove Items")
    print("3. View List")
    print("4. Exit")

    choice = input("Enter your Choice: ")
    if choice == "1":
        item = input("Enter Items: ")
        shopping_list.append()
        print("Item Added ")

    elif choice == "2":
        item = input("Remove Items: ")
        shopping_list.remove()
        print("Item Removed")

    elif choice == "3":
        print("Your Shopping List : ")
        for item in shopping_list:
            print(list)
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice! ")