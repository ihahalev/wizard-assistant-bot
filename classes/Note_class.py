import datetime
import pickle
from collections import UserDict


class Note:
    def __init__(self, title, content):
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

    def searchstring(self):
        tags_line = ' '.join(self.tags) if self.tags else ""
        return (self.content + " " + tags_line).lower()
    
    def search_tag(self):
        return ' '.join(self.tags).lower() if self.tags else ""
    
    def __str__(self):
         return f"Title: {self.title:^3}. DATE: {self.creation_date.strftime('%d.%m.%Y %H:%M')}. NOTE: {self.content} [Tags: {', '.join(self.tags)}]"


class NoteBook(UserDict):
    def __init__(self):
        self.data = UserDict()

    def add_record(self, note):
        self.data[note.title] = note
        

    def read_from_file(self):
        with open('data\\nbook.dat', 'rb') as fh:
            return pickle.load(fh)
        
    def save_to_file(self):
        with open('data\\nbook.dat', 'wb') as fh:
            pickle.dump(self, fh)

    def edit_record(self, args):
        self.data[args[0]].content = (' '.join(args[1:]))

    def del_note(self, args):
        self.data.pop(args[0])


nbook = NoteBook()
note = Note("Бред", "много текста ни о чем")
nbook.add_record(note)
print(note)
if "много текста ни о чем" in note.searchstring():
    print("Рядок знайдено.")
else:
    print("Рядок не знайдено.")

note.add_tag("маразм близко")

print(note)

if "маразм близко" in note.search_tag():
    print("Тег знайдено.")
else:
    print("Тег не знайдено.")

note.remove_tag("маразм близко")
print(note)