from collections import UserDict
from datetime import datetime, timedelta

from .Record import Record
from ..helpers.constants import format
from ..helpers.json_converter import to_json

class AddressBook(UserDict):
    def add_record(self, rec:Record):
        self.data[rec.name.value] = rec

    def find(self, name:str) -> Record:
        return self.data.get(name)

    def change_name(self, name:str, new_name:str):
        found = self.find(name)
        if not found:
            return "Contact not found."
        found.edit_name(new_name)
        self.remove_record(name)
        self.add_record(found)

    def remove_record(self, name:str):
        del self.data[name]

    def get_upcoming_birthdays(self, depth_days:int) -> list[dict]:
        today = datetime.today().date()
        b_users = []
        if depth_days < 0:
            x = depth_days
            y = 1
        else:
            x = 0
            y = depth_days + 1

        for rec in self.data.values():
            birth_date = rec.birthday.value if rec.birthday else None
            for day in range(x, y):
                b_day_on_this_day = datetime(year=(today+timedelta(days=day)).year, month=birth_date.month, day=birth_date.day).date()
                years_old = b_day_on_this_day.year - birth_date.year
                if (day == (b_day_on_this_day - today).days and years_old >= 0):      
                    b_users.append({"name": rec.name.value, "congratulation_date": b_day_on_this_day.strftime(format), "years_old": years_old})
        return b_users

    def __getstate__(self):
        attributes = self.__dict__
        return attributes

    def __setstate__(self, state):
        self.__dict__ = state

    def to_json(self):
        return to_json(self.data)

    @classmethod
    def from_json(cls, json_dict: dict):
        book = cls()
        for rec_info in json_dict.values():
            record = Record.from_json(rec_info)
            if record:
                book.add_record(record)
        return book