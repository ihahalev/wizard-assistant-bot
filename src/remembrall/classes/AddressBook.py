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

        for rec in self.data.values():
            birth_date = rec.birthday.value if rec.birthday else None
            t = today+timedelta(days=depth_days)
            print(t)
            b_day_current_year = datetime(year=(today+timedelta(days=depth_days)).year, month=birth_date.month, day=birth_date.day).date()
            b_day_current_year_pl7 = datetime(year=(today+timedelta(days=depth_days+7)).year, month=birth_date.month, day=birth_date.day).date()
            print(b_day_current_year_pl7 - b_day_current_year)
            if (-1 + depth_days) <= (b_day_current_year - today).days < (6 + depth_days):
                match b_day_current_year.weekday():
                    case 5:
                        b_day_current_year = b_day_current_year + timedelta(days=2)
                    case 6:
                        b_day_current_year = b_day_current_year + timedelta(days=1)        
                b_users.append({"name": rec.name.value, "congratulation_date": b_day_current_year.strftime(format)})
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