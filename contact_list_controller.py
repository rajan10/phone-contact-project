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

    def load_contacts(self, file_path: str) -> None:
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                self.contacts = [
                    Contact(**contact_data) for contact_data in data
                ]  # [Contact(name="Hari",phone=123),]
        except FileNotFoundError:
            self.contacts = []

    def search_contact(self, name: str) -> object:
        for contact in self.contacts:
            if contact.name == name:
                return contact


contacts = ContactList()


def take_inputs() -> tuple:
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    return name, phone  # returns tuple


def add_record() -> None:
    user_inputs = take_inputs()
    name, phone = user_inputs

    contact = Contact(name, phone)  # create an instance of Contact
    contacts.add_contact(contact)
    contacts.save_contact("phone_list.json")
    print("Recored added & saved Successfully!")


def search_record(name) -> None:
    contacts.load_contacts("phone_list.json")

    result_object = contacts.search_contact(name)
    if result_object:
        print(f"Name: {result_object.name}, Phone: {result_object.phone}")
    else:
        print("Contact not found.")
