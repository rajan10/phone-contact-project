from contact_list_controller import controller


def menu_display():
    while True:
        print("\nContact List Menu:")
        print("1. Add Contact")
        print("2. Search Contact By Name")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            controller.add_record()
        elif choice == "2":
            name = input("Enter name to search: ")
            controller.search_record(name)
        elif choice == "3":
            print("Exiting the Contact List. Goodbye!")
            break
        else:
            print("Invalid Choice. Please choose 1, 2, or 3.")
