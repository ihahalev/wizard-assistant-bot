from datetime import datetime
from collections import UserDict
from ..helpers.customErrors import NoteError
from ..helpers.json_converter import to_json
from ..helpers.constants import created_at_format

class Note:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content
        self.tags = list()
        self.created_at = datetime.now()

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)
        else:
            raise NoteError ('No Tag to remove')

    def get_tags_as_str(self) -> str:
        return ' '.join(self.tags).lower() if self.tags else ""

    def __str__(self) -> str:
        separator = "-" * 80
        return f"{separator}\nTitle: {self.title}\nContent: {self.content}\nTags: {', '.join(self.tags)}\nDate: {self.created_at.strftime(created_at_format)}\n{separator}"

    def to_json(self):
        return to_json(self.__dict__)

    @classmethod
    def from_json(cls, json_dict: dict):
        try:
            title = json_dict['title']
            content = json_dict['content']
            note = cls(title, content)
            try:
                tags = json_dict['tags']
                if type(tags) is list:
                    for tag in tags:
                        note.add_tag(tag)
                else:
                    note.add_tag(tags)
            except Exception:
                pass
            try:
                created_at = json_dict['created_at']
                note.created_at = datetime.strptime(created_at, created_at_format)
            except Exception as error:
                print(f"Creation date wrong format, creating new, {error}, {json_dict.get('created_at')}")
                note.created_at = datetime.now()
            return note
        except Exception as error:
            print(f"Note cannot be created, {type(error)}, {error}, {json_dict}")

class NoteBook(UserDict):
    def get_all_notes(self) -> list:
        return list(self.data.values())
    
    def add_note(self, note: Note):
        if self.find_note(note.title):
            raise NoteError("This title exists")
        self.data[note.title] = note
        
    def edit_note(self, title: str, new_context: str):
        found = self.find_note(title)
        if not found:
            raise NoteError("This title doesn't exist")
        self.data[title].content = new_context

    def remove_note(self, title: str):
        if not self.find_note(title):
            raise NoteError("This title doesn't exist")
        self.data.pop(title)

    def change_title(self, title: str, new_title: str):
        found = self.find_note(title)
        if not found:
            raise NoteError("This title doesn't exist")
        found.title = new_title
        self.remove_note(title)
        self.add_note(found)

    def find_note(self, title: str) -> Note:
        return self.data.get(title)

    def find_with_content(self, search_str: str) -> list[Note]:
        notes = self.data.values()
        return [n for n in notes if search_str.lower() in n.content.lower()]

    def find_with_tag(self, search_tag: str) -> list[Note]:
        notes = self.data.values()
        return [n for n in notes if search_tag.lower() in n.get_tags_as_str()]

    def to_json(self):
        return to_json(self.data)

    @classmethod
    def from_json(cls, json_dict: dict):
        book = cls()
        for note_info in json_dict.values():
            note = Note.from_json(note_info)
            if note:
                book.add_note(note)
        return book
