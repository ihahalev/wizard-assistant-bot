from .wrappers import input_error
from ..classes import AddressBook, Record

@input_error
def add_contact(args, book: AddressBook):
    name, phone = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        err = record.add_phone(phone)
        if err:
            if message == "Contact added.":
                print(err)
                message = "Contact added without phone"
            else:
                message = err
    return message

@input_error
def change_contact(args: list, book: AddressBook) -> str:
    name, new_name = args
    found = book.find(name)
    if not found:
        return "Contact not found."
    book.change_name(name, new_name)
    return "Contact updated."

@input_error
def remove_contact(args: list, book: AddressBook) -> str:
    name = args[0]
    found = book.find(name)
    if not found:
        return "Contact not found."
    book.remove_record(name)
    return "Contact removed."

@input_error
def change_phone(args: list, book: AddressBook) -> str:
    name, phone, new_phone = args
    found = book.find(name)
    if not found:
        return "Contact not found."
    found.edit_phone(phone, new_phone)
    return "Contact updated."

@input_error
def remove_phone(args: list, book: AddressBook) -> str:
    name, phone = args
    found = book.find(name)
    if not found:
        return "Contact not found."
    found.remove_phone(phone)
    return "Contact updated."

@input_error
def get_contact_phones(args: list, book: AddressBook) -> str:
    name = args[0]
    found = book.find(name)
    if not found:
        return "Contact not found."
    if not found.phones:
        return "Contact has no phone numbers."
    return f"{'; '.join(p.value for p in found.phones if p.value)}"

@input_error
def get_all_contacts(book: AddressBook) -> str:
    if not len(book):
        return "Address book is empty"
    output = "Address book:"
    for record in book.data.values():
        output += f"\n{record}"
    return output

@input_error
def add_birthday(args: list, book: AddressBook) -> str:
    name, birthday = args
    found = book.find(name)
    if not found:
        return "Contact not found."
    found.add_birthday(birthday)
    return "Birthday added"

@input_error
def show_birthday(args: list, book: AddressBook) -> str:
    name = args[0]
    found = book.find(name)
    if not found:
        return "Contact not found."
    if not found.birthday:
        return "Contact has no birthday date."
    return found.birthday

@input_error
def change_birthday(args: list, book: AddressBook) -> str:
    name, birthday = args
    found = book.find(name)
    if not found:
        return "Contact not found."
    found.edit_birthday(birthday)
    return "Birthday changed"

@input_error
def get_birthdays(args: list, book: AddressBook) -> str:
    days = int(args[0])
    if not len(book):
        return "Address book is empty"
    birthdays = book.get_upcoming_birthdays(days)
    if not birthdays:
        return "No upcoming birthdays"
    output = "Upcoming birthdays:"
    for record in birthdays:
        output += f"\n{record}"
    return output

@input_error
def add_email(args: list, book: AddressBook) -> str:
    name, email = args
    found = book.find(name)
    if not found:
        return "Contact not found."
    found.add_email(email)
    return "Email added"

@input_error
def change_email(args: list, book: AddressBook) -> str:
    name, input, new_email = args
    found = book.find(name)
    if not found:
        return "Contact not found."
    found.edit_email(input, new_email)
    return "Email changed"

@input_error
def remove_email(args: list, book: AddressBook) -> str:
    name, email = args
    found = book.find(name)
    if not found:
        return "Contact not found."
    found.remove_email(email)
    return "Email updated."

@input_error
def add_address(args: list, book: AddressBook) -> str:
    '''Add address to a contact. If contact does not exist, return "Contact not found."
    If address is already present, return "Address already exists."
    If address is added, return "Address added."
    '''
    if len(args) < 1:
        raise IndexError()
    name, address = ' '.join(args).split(' ', 1)
    if not address:
        raise ValueError()
    found = book.find(name)
    if not found:
        return "Contact not found."
    if found.address:
        return "Address already exists."
    found.add_address(address)
    return "Address added."

@input_error
def change_address(args: list, book: AddressBook) -> str:
    '''Edit address of a contact. If contact does not exist, return "Contact not found."
    If address is not present, return "No address to edit."
    If address is edited, return "Address updated."
    '''
    if len(args) < 1:
        raise IndexError()
    name, address = ' '.join(args).split(' ', 1)
    if not address:
        raise ValueError()
    found = book.find(name)
    if not found:
        return "Contact not found."
    if found.address:
        found.change_address(address)
        return "Address changed."
    found.add_address(address)
    return "Address added."

@input_error
def remove_address(args: list, book: AddressBook) -> str:
    '''Delete address of a contact. If contact does not exist, return "Contact not found.
    If address is not present, return "No address to delete."
    If address is deleted, return "Address deleted."
    '''
    name = args[0]
    found = book.find(name)
    if not found:
        return "Contact not found."
    if found.address:
        found.remove_address()
        return "Address deleted."
    return "No address to delete."

@input_error
def get_all_notes(book: AddressBook) -> str:
    # TODO: Get all notes from book
    return ["Note 1"]

@input_error
def add_note(args: list, book: AddressBook) -> str:
    title, text = args
    # TODO: Add note to book
    return "Note added"

@input_error
def show_note(args: list, book: AddressBook) -> str:
    title = args
    # TODO: Show note (found by title) from book
    return "Note"

@input_error
def change_note(args: list, book: AddressBook) -> str:
    title, text = args
    # TODO: Change note in book
    return "Note changed"

@input_error
def remove_note(args: list, book: AddressBook) -> str:
    title = args
    # TODO: Remove note from book
    return "Note removed"

@input_error
def change_note_title(args: list, book: AddressBook) -> str:
    title, new_title = args
    # TODO: Change note title in book
    return "Note title changed"

@input_error
def add_note_tag(args: list, book: AddressBook) -> str:
    title, tag = args
    # TODO: Add tag to note
    return "Tag added"

@input_error
def change_note_tag(args: list, book: AddressBook) -> str:
    title, tag, new_tag = args
    # TODO: Change tag in note
    return "Tag changed"

@input_error
def remove_note_tag(args: list, book: AddressBook) -> str:
    title, tag = args
    # TODO: Remove tag from note
    return "Tag removed"