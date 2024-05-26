from .wrappers import input_error, note_error
from ..classes import AddressBook, Record, NoteBook, Note

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
def show_contact(args: list, book: AddressBook) -> str:
    name = args[0]
    found = book.find(name)
    if not found:
        return "Contact not found."
    return str(found)

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
    if not args[0]:
        return
    days = int(args[0])
    if not len(book):
        return "Address book is empty"
    birthdays = book.get_upcoming_birthdays(days)
    if not birthdays:
        if days < 0:
            return "No past birthdays"
        else:
            return "No upcoming birthdays"
    if days < 0:
        output = "Past birthdays:"
    else:
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

@note_error
def get_all_notes(notebook: NoteBook) -> str:
    '''
    Get all notes from the notebook. If notebook is empty, return "Note book is empty."
    If notes are present, return all notes in the format:
    "All Notes:
    Title: title1 | Tags: tag1, tag2 | Content: content1 | Date: date1
    Title: title2 | Tags: tag1, tag2 | Content: content2 | Date: date2
    '''
    notes = notebook.get_all_notes()
    if not notes:
        return "Note book is empty."
    output = "All Notes:"
    for note in notes:
        output += f"\n{note}"
    return output


@note_error
def add_note(args: list, notebook: NoteBook) -> str:
    '''Add a note to the notebook. If note with the same title exists, return 
    "Note with this title exists." If note is added, return "Note added."
    '''
    title = args[0]
    text = ' '.join(args[1:])
    note = Note(title, text)
    notebook.add_note(note)
    return "Note added."

@note_error
def show_note(args: list, book: NoteBook) -> str:
    '''Show a note with the given title. If note is not found, return "Note not found."
    If note is found, return the note in the format:
    "Title: title | Tags: tag1, tag2 | Content: content | Date: date"
    '''
    title = args[0]
    note = book.find_note(title)
    if not note:
        return "Note not found."
    return str(note)

@note_error
def change_note(args: list, book: NoteBook) -> str:
    '''Change the text of a note. If note is not found, return "Note not found."
    If note is found, change the text and return "Note updated."
    '''
    title, new_text = args
    book.edit_note(title, new_text)
    return "Note updated."

@note_error
def remove_note(args: list, book: NoteBook) -> str:
    '''Remove a note with the given title. If note is not found, return "Note not found."
    If note is found, remove the note and return "Note removed."
    '''
    title = args[0]
    book.remove_note(title)
    return "Note removed."

@note_error
def change_note_title(args: list, book: NoteBook) -> str:
    '''Change the title of a note. If note is not found, return "Note not found."
    If note is found, change the title and return "Note title changed."
    '''
    title, new_title = args
    book.change_title(title, new_title)
    return "Note title changed."

@note_error
def add_note_tag(args: list, book: NoteBook) -> str:
    '''Add a tag to a note. If note is not found, return "Note not found."
    If tag is added, return "Tag added."
    '''
    title, tag = args
    note = book.find_note(title)
    if not note:
        return "Note not found."
    note.add_tag(tag)
    return "Tag added"

@note_error
def remove_note_tag(args: list, book: NoteBook) -> str:
    '''Remove a tag from a note. If note is not found, return "Note not found."
    If tag is removed, return "Tag removed."
    '''
    title, tag = args
    note = book.find_note(title)
    note.remove_tag(tag)
    return "Tag removed"

@note_error
def sort_notes_by_tags(search_tags: list, notebook: NoteBook) -> str:
    '''Sort notes by tags. If no tags are given, return "Please give a tags."
    If notes are found, return all notes with the given tags in the format:
    "Title: title1 | Tags: tag1, tag2 | Content: content1 | Date: date1
    Title: title2 | Tags: tag1, tag2 | Content: content2 | Date: date2"
    '''
    if not search_tags:
        return "Please give a tags."
    notes = []
    for tag in search_tags:
        notes.extend(notebook.find_with_tag(tag)) 
    if not notes:
        return "No notes found with the given tags."
    notes = list(set(notes))

    # Sort notes by the number of matching tags, then by the total number of tags, and finally by the date
    sorted_notes = sorted(notes, key=lambda note: (-len(set(note.tags) & set(search_tags)), -len(note.tags), note.date), reverse=True)

    return '\n'.join(str(note) for note in sorted_notes)

@note_error
def find_notes_with_content(search_str: str, notebook: NoteBook) -> str:
    '''Find notes with the given content. If no content is given, return "Please give a content."
    If notes are found, return all notes with the given content in the format:
    "Title: title1 | Tags: tag1, tag2 | Content: content1 | Date: date1"
    '''
    if not search_str:
        return "Please give a content."
    notes = notebook.find_with_content(search_str)
    if not notes:
        return "No notes found with the given content."
    return '\n'.join(str(note) for note in notes)
