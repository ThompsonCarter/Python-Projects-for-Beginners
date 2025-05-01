# Hands-On Project: Build a Contact Book
def add_contact(contact_book):
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contact_book[name] = {"phone": phone, "email": email}
    print(f"Contact for {name} added successfully!")

def update_contact(contact_book):
    name = input("Enter the name of the contact to update: ")
    if name in contact_book:
        phone = input(f"Enter new phone number for {name}: ")
        email = input(f"Enter new email address for {name}: ")
        contact_book[name] = {"phone": phone, "email": email}
        print(f"Contact for {name} updated successfully!")
    else:
        print(f"Contact for {name} not found.")

def search_contact(contact_book):
    name = input("Enter the name of the contact to search for: ")
    if name in contact_book:
        print(f"Contact Details for {name}:")
        print(f"Phone: {contact_book[name]['phone']}")
        print(f"Email: {contact_book[name]['email']}")
    else:
        print(f"Contact for {name} not found.")

def main():
    contact_book = {}
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contact_book)
        elif choice == "2":
            update_contact(contact_book)
        elif choice == "3":
            search_contact(contact_book)
        elif choice == "4":
            print("Exiting the Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
