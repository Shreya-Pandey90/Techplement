import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return

    if name in contacts:
        print("Contact already exists!")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    
    if not phone.isdigit():
        print("Invalid phone number! Must contain digits only.")
        return
    
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully!")

# Search for a contact
def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"\nName: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}\n")
    else:
        print("Contact not found.")

# Update contact
def update_contact(contacts):
    name = input("Enter name to update: ").strip()
    if name in contacts:
        phone = input("Enter new phone number (leave blank to keep old): ").strip()
        email = input("Enter new email (leave blank to keep old): ").strip()

        if phone:
            if not phone.isdigit():
                print("Invalid phone number! Must contain digits only.")
                return
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email

        print(f"Contact '{name}' updated successfully!")
    else:
        print("Contact not found.")

# Display all contacts
def display_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    for name, info in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")

# Main program loop
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Display All Contacts")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            display_contacts(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
