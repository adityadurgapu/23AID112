shopping_list = []

while True:
    action = input("What do you want to do? (add/remove/show/quit): ").lower()

    if action == "add":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"{item} added to the list.")

    elif action == "remove":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from the list.")
        else:
            print(f"{item} not found in the list.")

    elif action == "show":
        if shopping_list:
            print("Your shopping list:")
            index = 1
            for item in shopping_list:
                print(str(index) + ". " + item)
                index += 1
        else:
            print("Your shopping list is empty.")

    elif action == "quit":
        print("Exiting Shopping List Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please type add/remove/show/quit.")
