import pickle, json
from pathlib import Path
from typing import Callable

from .wrappers import file_read_error
from ..classes import AddressBook, NoteBook
from .constants import storage_link

def save_data(book: AddressBook, note_book:NoteBook, filename="wizard_assistant.pkl"):
    try:
        if not len(book):
            return
        storage = Path.cwd()/storage_link
        storage.mkdir(exist_ok=True, parents=True)
        file = storage/filename
        file_type = input("To what format save data (B - binary, J - JSON): ")
        match file_type.lower():
            case "j":
                save_json_data(book, note_book, str(file.with_suffix(".json")))
            case "b":
                save_binary_data(book, note_book, str(file))
            case _:
                save_binary_data(book, note_book, str(file))
    except Exception as error:
        print(f"Error occured on create file, {type(error)}, {error}")

def save_binary_data(book: AddressBook, note_book:NoteBook, filename: str):
    books = {"records": book, "notes": note_book}
    with open(filename, "wb") as f:
        pickle.dump(books, f)

def save_json_data(book: AddressBook, note_book:NoteBook, filename: str):
    notes = note_book.to_json()
    books =  {"records": book.to_json(), "notes": notes}
    with open(filename, "w") as f:
        json.dump(books, f)

def load_data(filename="wizard_assistant.pkl"):
    storage = Path.cwd()/storage_link
    if not storage.exists():
        print("No storage directory with data")
        book = AddressBook()
        note_book = NoteBook()
        return book, note_book
    has_files = any(p.is_file() for p in storage.iterdir())
    if not has_files:
        print("No files to upload")
        book = AddressBook()
        note_book = NoteBook()
        return book, note_book
    file = storage/filename
    file_type = input("From what format load data (B - binary, J - JSON): ")
    match file_type.lower():
        case "j":
            books = fallback_loader(str(file.with_suffix(".json")), str(file), load_json_data, load_binary_data)
        case "b":
            books = fallback_loader(str(file), str(file.with_suffix(".json")), load_binary_data, load_json_data)
        case _:
            books = fallback_loader(str(file), str(file.with_suffix(".json")), load_binary_data, load_json_data)
    return books

def fallback_loader(
        primary_file: str,
        fallback_file: str,
        primary_fn: Callable[[str], dict],
        fallback_fn: Callable[[str], dict]
) -> AddressBook:
    books = primary_fn(primary_file)
    if not books:
        books = fallback_fn(fallback_file)
        if not books:
            addr_book = AddressBook()
            note_book = NoteBook()
        else:
            addr_book = books.get("records")
            note_book = books.get("notes")
    else:
        addr_book = books.get("records")
        note_book = books.get("notes")
    if not addr_book:
        addr_book = AddressBook()
    if not note_book:
        note_book = NoteBook()
    return addr_book, note_book

@file_read_error
def load_binary_data(filename="wizard_assistant.pkl") -> dict | None:
    with open(filename, "rb") as f:
        return pickle.load(f)

@file_read_error
def load_json_data(filename="wizard_assistant.json") -> dict | None:
    with open(filename, "r") as f:
        json_data = json.load(f)
    if json_data:
        try:
            records = json_data["records"]
            addr_book = AddressBook.from_json(records)
        except Exception:
            addr_book = None
        try:
            notes = json_data["notes"]
            note_book = NoteBook.from_json(notes)
        except Exception:
            note_book = None
        return {"records": addr_book, "notes": note_book}
