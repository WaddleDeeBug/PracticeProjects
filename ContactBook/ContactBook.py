def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

contact_book = {}

def add_contact(contact_book):
    print("\n--- Add Contact ---")
    name = input("Enter contact name: ")
    if name in contact_book:
        print("Contact already exists!")
    else:
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("enter address: ")

        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added successfully!")

def view_contact(contact_book):
    print("\n--- View Contact ---")
    name = input("Enter contact name to view: ")
    if name in contact_book:
        contact = contact_book[name]
        print("Name:", name)
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("Address:", contact["address"])
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    print("\n--- Edit Contact ---")
    name = input("Enter contact name to edit: ")
    if name in contact_book:
        phone = input(f"Enter new phone number (press enter to keep current: {contact_book[name]['phone']}): ")
        email = input(f"Enter new email address (press enter to keep current: {contact_book[name]['email']}): ")
        address = input(f"Enter new address (press enter to keep current: {contact_book[name]['address']}): ")

        #Checks if the user provided input; if not, keeps the current value
        if phone == '':
            phone = contact_book[name]['phone']
        if email == '':
            email = contact_book[name]['email']
        if address == '':
            address = contact_book[name]['address']

        contact_book[name] = {"phone": phone, "email": email, "address": address}
        print("Contact updated successfully!")
    else:
        print("Contact not found!")    

def delete_contact(contact_book):
    print("\n--- Delete Contact ---")
    name = input("Enter contact name to delete: ")
    if name in contact_book:
        confirm = input(f"Are you sure you want to delete {name}? (Yes/No): ").lower()
        if confirm == 'Yes':
            del contact_book[name]
            print("Contact deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print("Contact not found!")

def list_all_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
    else:
        for name, info in contact_book.items():
            print("Name:", name)
            print("Phone:", info["phone"])
            print("Email:", info["email"])
            print("Address:", info["address"])
            print() #Blank line

#Navigation menu:
while True:
    display_menu()
    choice = input()
    if choice == "1":
        add_contact(contact_book)
    elif choice == "2":
        view_contact(contact_book)
    elif choice == "3":
        edit_contact(contact_book)
    elif choice == "4":
        delete_contact(contact_book)
    elif choice == "5":
        list_all_contacts(contact_book)
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")