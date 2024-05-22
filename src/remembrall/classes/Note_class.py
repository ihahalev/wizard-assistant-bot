import datetime
from collections import UserDict
from remembrall.classes.customErrors import NoteError


class Note:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content
        self.tags = list()
        self.creation_date = datetime.datetime.now()
    
    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)
    
    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)
        else:
            raise NameError

    def get_tags_as_str(self) -> str:
        return ' '.join(self.tags).lower() if self.tags else ""

    def __str__(self) -> str:
        return f"Title: {self.title:^2}| Tags: {', '.join(self.tags):>20} | {self.content:<70}"


class NoteBook(UserDict):
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

    def find_with_context(self, search_str: str) -> list[Note]:
        notes = self.data.values()
        return [note for n in notes if search_str.lower() in n.content.lower()]

    def find_with_tag(self, search_tag: str) -> list[Note]:
        notes = self.data.values()
        return [note for n in notes if search_tag.lower() in n.get_tags_as_str()]