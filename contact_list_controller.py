import json


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class ContactList:
    def __init__(self):
        self.contacts = []

        # load the json when object is created

    def add_contact(self, contact: object) -> None:
        self.contacts.append(contact)

    def save_contact(self, file_name: str) -> None:
        with open(file_name, "w") as file:
            json.dump([vars(contact) for contact in self.contacts], file)

    def search_contact(self, name: str) -> object:
        for contact in self.contacts:
            if contact.name == name:
                return contact


contacts = ContactList()


def add_record():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contact = Contact(name, phone)  # create an instance of Contact
    contacts = ContactList()  # Create an instance of ContactList
    contacts.add_contact(contact)
    contacts.save_contact("phone_list.json")
    print("Recored added & saved Successfully!")


def search_record(name):
    search_name = contacts.search_contact(name)
    if search_name:
        print(f"Name: {search_name.name}, Phone: {search_name.phone}")
    else:
        print("Contact not found.")
