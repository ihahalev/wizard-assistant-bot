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

import sys
from remembrall.classes import Record
from remembrall.helpers import book_operations
from remembrall.helpers.data_upload import load_data, save_data

def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main(test_users = None):
    book = load_data()
    load_test = len(sys.argv)>1 and sys.argv =="test" and test_users and not book.data
    if load_test:
        for user in test_users:
            rec = Record(user['name'])
            if user['phone']:
                rec.add_phone(user['phone'])
            if user['birthday']:
                rec.add_birthday(user['birthday'])
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
                # show contacts with all info about them
                print(book_operations.get_all_contacts(book))
            case "add-contact":
                # add contact by name with phone
                print(book_operations.add_contact(args, book))
            case "show-contact":
                # show contact with all info
                pass
            case "change-contact":
                # change contact name
                print(book_operations.change_contact(args, book))
            case "remove-contact":
                # remove contact
                print(book_operations.remove_contact(args, book))
            case "change-phone":
                # change contact phone
                print(book_operations.change_phone(args, book))
            case "remove-phone":
                # remove contact phone
                print(book_operations.add_birthday(args, book))
            case "add-birthday":
                # add contact birthday
                print(book_operations.add_birthday(args, book))
            case "change-birthday":
                # change contact birthday
                print(book_operations.add_birthday(args, book))
            case "birthdays":
                # get upcoming birthdays
                print(book_operations.get_birthdays(args, book))
            case "add-email":
                # add contact email
                pass
            case "change-email":
                # change contact email
                pass
            case "add-address":
                # add contact address
                pass
            case "change-address":
                # change contact address
                pass
            case "add-note":
                # add note with title and text
                pass
            case "show-note":
                # show note with all info
                pass
            case "change-note":
                # change note text
                pass
            case "remove-note":
                # remove note
                pass
            case "change-title":
                # change note title
                pass
            case "add-tag":
                # add note tag
                pass
            case "change-tag":
                # change note tag
                pass
            case "remove-tag":
                # remove note tag
                pass
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    users = [
        {"name": "Doe", "phone": "", "birthday": "21.01.1985"},
        {"name": "John", "phone": "0987654321", "birthday": ""},
        {"name": "John Doe", "phone": "7894561230", "birthday": "23.01.1985"},
        {"name": "Jane Smith", "phone": "1234567890", "birthday": "27.01.1990"},
        {"name": "Jane", "phone": "3216549870", "birthday": "28.01.1990"},
        {"name": "Smith", "phone": "0321654987", "birthday": "29.01.1990"}
    ]
    main(users)