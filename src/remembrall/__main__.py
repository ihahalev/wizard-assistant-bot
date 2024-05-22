"""Assistant bot for wizards of the academy.

Usage:
--------

    $ remembrall [command] [args1, args2, ...]

List the avaialble commands:

    $ remembrall help

Version:
--------

- wizards-remembrall v1.0.0
"""
from classes import Record
from helpers import book_operations
from helpers.data_upload import load_data, save_data

def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main(test_users = None):
    book = load_data()
    if test_users and not book.data:
        for user in test_users:
            rec = Record(user['name'])
            if user['phone']:
                rec.add_phone(user['phone'])
            if user['birthday']:
                rec.add_birthday(user['birthday'])
            if user['address']:
                rec.add_address(user['address'])
            book.add_record(rec)
        print("Test data added")
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                save_data(book)
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "all-contacts":
                print(book_operations.get_all_contacts(book))
            case "add-contact":
                print(book_operations.add_contact(args, book))
            case "change-contact":
                print(book_operations.change_contact(args, book))
            case "show-phones":
                print(book_operations.get_contact_phones(args, book))
            case"add-birthday":
                print(book_operations.add_birthday(args, book))
            case "show-birthday":
                print(book_operations.show_birthday(args, book))
            case "birthdays":
                print(book_operations.get_birthdays(book))
            case "add-address":
                print(book_operations.add_address(args, book))
            case "change-address":
                print(book_operations.edit_address(args, book))
            case "remove-address":
                print(book_operations.delete_address(args, book))
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    users = [
        {"name": "Doe", "phone": "", "birthday": "21.01.1985", "address": "123 Maple St"},
        {"name": "John", "phone": "0987654321", "birthday": "", "address": "456 Elm St"},
        {"name": "John Doe", "phone": "7894561230", "birthday": "23.01.1985", "address": "789 Oak St"},
        {"name": "Jane Smith", "phone": "1234567890", "birthday": "27.01.1990", "address": "987 Pine St"},
        {"name": "Jane", "phone": "3216549870", "birthday": "28.01.1990", "address": "654 Birch St"},
        {"name": "Smith", "phone": "0321654987", "birthday": "29.01.1990", "address": "321 Cedar St"}
    ]
    main(users)
