from contact_list_controller import add_record, search_record


def menu_display():
    while True:
        print("\nContact List Menu:")
        print("1. Add Contact")
        print("2. Search Contact By Name")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("you chose 1")
            add_record()
        elif choice == "2":
            print("you chose 2")
            name_search = input("enter Name to search")
            search_record(name_search)
        else:
            print("Invalid Choice. Please choose 1,2,3 and r or quit.")
            break
