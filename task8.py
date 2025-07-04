#Dynamic Contact Book Using Dictionaries

def is_valid_email(email):
    # Simple email validation
    return "@" in email and "." in email

def manage_contact_book():
    contact_book = {}

    while True:
        print("\nContact Book Menu:")
        print("1. Add new contact")
        print("2. Update existing contact")
        print("3. View all contacts")
        print("4. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            name = input("Enter contact name: ").strip().title()
            if name in contact_book:
                print("Contact already exists.")
                continue
            phone = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            if not is_valid_email(email):
                print("Invalid email format.")
                continue
            contact_book[name] = {"phone": phone, "email": email}
            print(f"Contact for {name} added.")

        elif choice == "2":
            name = input("Enter contact name to update: ").strip().title()
            if name not in contact_book:
                print("Contact not found.")
                continue
            phone = input("Enter new phone number (leave blank to keep current): ").strip()
            email = input("Enter new email (leave blank to keep current): ").strip()
            if phone:
                contact_book[name]["phone"] = phone
            if email:
                if not is_valid_email(email):
                    print("Invalid email format. Email not updated.")
                else:
                    contact_book[name]["email"] = email
            print(f"Contact for {name} updated.")

        elif choice == "3":
            name = input("Enter contact name to retrieve: ").strip().title()
            if name in contact_book:
                info = contact_book[name]
                print(f"{name}: Phone: {info['phone']}, Email: {info['email']}")
            else:
                print("Contact not found.")

        elif choice == "4":
            if not contact_book:
                print("No contacts to display.")
            else:
                print("\nAll Contacts:")
                for idx, (name, info) in enumerate(contact_book.items(), 1):
                    print(f"{idx}. {name} - Phone: {info['phone']}, Email: {info['email']}")

        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please select from 1 to 5.")

# Run the contact book manager
manage_contact_book()
