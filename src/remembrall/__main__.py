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
from datetime import datetime
from remembrall.classes import Record, Note
from remembrall.helpers import book_operations
from remembrall.helpers.data_upload import load_data, save_data
from remembrall.helpers.greeting import farewell, greeting
from remembrall.helpers.help_function import show_help
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from remembrall.helpers.intellectual_analysis import session
from remembrall.helpers.constants import created_at_format
from colorama import Fore, Style
def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main(test_users = None, test_notes = None):
    book, note_book = load_data()
    load_test = len(sys.argv)>1 and sys.argv[1] =="test"
    add_test = False
    if load_test:
        if test_users and not book.data:
            add_test = True
            for user in test_users:
                rec = Record(user['name'])
                if user['phone']:
                    rec.add_phone(user['phone'])
                if user['birthday']:
                    rec.add_birthday(user['birthday'])
                if user['address']:
                    rec.add_address(user['address'])
                if user['email']:
                    rec.add_email(user['email'])
                book.add_record(rec)
        if test_notes and not note_book.data:
            add_test = True
            for note in test_notes:
                rec = Note(note['title'], note['content'])
                if note['tag']:
                    rec.add_tag(note['tag'])
                if note['created_at']:
                    rec.created_at = datetime.strptime(note['created_at'], created_at_format)
                note_book.add_note(rec)
        if add_test:
            print("Test data added")
    greeting()
    print(Fore.BLUE + "Welcome to the Assistant bot for wizards of the academy!")
    print('Type |help| to see all bot commands' + Style.RESET_ALL)
    
    while True:
        user_input = session.prompt("Enter a command: ", auto_suggest=AutoSuggestFromHistory(), complete_while_typing=False)
        if not user_input:
            print("No command provided")
            continue
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                save_data(book, note_book)
                farewell()
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
                print(book_operations.show_contact(args, book))
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
                print(book_operations.remove_phone(args, book))
            case "add-birthday":
                # add contact birthday
                print(book_operations.add_birthday(args, book))
            case "change-birthday":
                # change contact birthday
                print(book_operations.change_birthday(args, book))
            case "birthdays":
                # get upcoming birthdays
                print(book_operations.get_birthdays(args, book))
            case "add-email":
                # add contact email
                print(book_operations.add_email(args, book))
            case "change-email":
                # change contact email
                print(book_operations.change_email(args, book))
            case "remove-email":
                # change contact email
                print(book_operations.remove_email(args, book))                
            case "add-address":
                # add contact address
                print(book_operations.add_address(args, book))
            case "change-address":
                # change contact address
                print(book_operations.change_address(args, book))
            case "remove-address":
                # remove contact address
                print(book_operations.remove_address(args, book))
            case "all-notes":
                # show all notes
                print(book_operations.get_all_notes(note_book))
            case "add-note":
                # add note with title and text
                print(book_operations.add_note(args, note_book))
            case "show-note":
                # show note with all info
                print(book_operations.show_note(args, note_book))
            case "change-note":
                # change note text
                print(book_operations.change_note(args, note_book))
            case "remove-note":
                # remove note
                print(book_operations.remove_note(args, note_book))
            case "change-title":
                # change note title
                print(book_operations.change_note_title(args, note_book))
            case "add-tag":
                # add note tag
                print(book_operations.add_note_tag(args, note_book))
            case "remove-tag":
                # remove note tag
                print(book_operations.remove_note_tag(args, note_book))
            case "sort-tags":
                # sort notes by tags
                print(book_operations.sort_notes_by_tags(args, note_book))
            case "find-content":
                # find notes by content
                print(book_operations.find_notes_with_content(args, note_book))
            case "help":
                show_help()
            case _:

                print("Invalid command.")

if __name__ == "__main__":
    
    users = [
    {"name": "Harry", "phone": "0201234567", "birthday": "31.07.1980", "address": "4 Privet Drive, Little Whinging", "email": "harry.potter@hogwarts.edu"},
    {"name": "Hermione", "phone": "0202345678", "birthday": "19.09.1979", "address": "Hampstead Garden Suburb, London", "email": "hermione.granger@hogwarts.edu"},
    {"name": "Ron", "phone": "0203456789", "birthday": "01.03.1980", "address": "The Burrow, Ottery St Catchpole", "email": "ron.weasley@hogwarts.edu"},
    {"name": "Draco", "phone": "0204567890", "birthday": "05.06.1980", "address": "Malfoy Manor, Wiltshire", "email": "draco.malfoy@hogwarts.edu"},
    {"name": "Luna", "phone": "0205678901", "birthday": "13.02.1981", "address": "The Rookery, Ottery St Catchpole", "email": "luna.lovegood@hogwarts.edu"},
    {"name": "Neville", "phone": "0206789012", "birthday": "30.07.1980", "address": "Gran's House, London", "email": "neville.longbottom@hogwarts.edu"}
    ]

    notes = [
    {"title": "Avada", "content": "One of the Unforgivable Curses, causes instant death.", "tag": "DarkArts", "created_at": "21.01.2024.12.30"},
    {"title": "Cruciatus", "content": "Inflicts unbearable pain on the victim.", "tag": "DarkArts,Torture", "created_at": "21.01.2024.12.00"},
    {"title": "Imperius", "content": "Allows the caster to control the victim's actions.", "tag": "DarkArts,Control", "created_at": "21.01.2024.11.45"},
    {"title": "Expelliarmus", "content": "Disarms an opponent, forcing them to release whatever they are holding.", "tag": "Defense,Disarm", "created_at": "21.01.2024.11.30"},
    {"title": "Expecto", "content": "Summons a Patronus to ward off Dementors.", "tag": "Defense,Patronus", "created_at": "21.01.2024.11.15"},
    {"title": "Alohomora", "content": "Unlocks doors and other locked objects.", "tag": "Charms,Unlocking", "created_at": "21.01.2024.11.00"}
    ]

    main(users, notes)
