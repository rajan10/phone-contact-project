import json


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class ContactList:  # object will be initialize with file name 'phone_list.json' and in dict format
    def __init__(self, file="phone_list.json"):
        self.contacts = []
        self.file = file
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.file, "r") as file:
                data = json.load(file)
                self.contacts = [
                    Contact(**contact_data) for contact_data in data
                ]  # into dict
        except FileNotFoundError:
            self.contacts = []

    def save_contacts(self):
        with open(self.file, "w") as file:
            json.dump([vars(contact) for contact in self.contacts], file)

    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)  # appends in json format with keys and values
        self.save_contacts()  # will save in dictionary format

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None


def take_inputs() -> tuple:
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    return name, phone


class ContactController:
    def __init__(self, contact_list):
        self.contact_list = contact_list

    def add_record(self):
        user_inputs = take_inputs()
        name, phone = user_inputs
        self.contact_list.add_contact(name, phone)
        print("Record added & saved Successfully!")

    def search_record(self, name):
        result_contact = self.contact_list.search_contact(name)
        if result_contact:
            print(f"Name: {result_contact.name}, Phone: {result_contact.phone}")
        else:
            print("Contact not found.")


contacts = ContactList()
controller = ContactController(contacts)
