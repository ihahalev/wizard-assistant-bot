from .Fields import Name, Phone, Birthday, Address
from .customErrors import PhoneValidationError
from ..helpers.wrappers import input_error
from ..helpers.json_converter import to_json

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday = None
        self.address = None

    def __str__(self):
        name = f"name: {self.name.value}"
        phones = f"phones: {'; '.join(p.value for p in self.phones if p.value)}"
        birthday = f"birthday: {self.birthday if self.birthday else ''}"
        address = f"address: {self.address if self.address else ''}"
        return f"Contact {name}, {phones}, {birthday}, {address}"

    def edit_name(self, name:str):
        self.name.edit_name(name)

    @input_error
    def add_phone(self, phone_number: str):
        if not [phone for phone in self.phones if phone.value == phone_number]:
            self.phones.append(Phone(phone_number))

    def find_phone(self, phone_number:str) -> Phone:
        for phone in self.phones:
            if phone.value == phone_number:
                return phone

    def edit_phone(self, old_phone:str, new_phone:str):
        found_phone = self.find_phone(old_phone)
        if not found_phone:
            raise PhoneValidationError("Phone number not found")
        found_phone.edit_phone(new_phone)

    def remove_phone(self, phone):
        found_phone = self.find_phone(phone)
        self.phones.remove(found_phone)

    def add_birthday(self, birthday):
        if not self.birthday:
            self.birthday = Birthday(birthday)

    def edit_birthday(self, birthday:str):
        if not self.birthday:
            self.birthday = Birthday(birthday)
        else:
            self.birthday.edit_birthday(birthday)

    def add_address(self, address):
        if not self.address:
            self.address = Address(address)
            return "Address added."
        return "Address already exists."

    def change_address(self, new_address):
        if self.address:
            self.address.change_address(new_address)
            return "Address changed."
        self.add_address(new_address)
        return "Address added."
    
    def remove_address(self):
        if self.address:
            self.address = None
            return "Address deleted."
        return "No address to delete."
           
    def __getstate__(self):
        attributes = self.__dict__
        return attributes

    def __setstate__(self, state):
        self.__dict__ = state

    def to_json(self):
        return to_json(self.__dict__)

    @classmethod
    def from_json(cls, json_dict: dict):
        try:
            name = json_dict['name']['value']
            record = cls(name)
            try:
                phones = json_dict['phones']
                if type(phones) is list:
                    for phone in phones:
                        record.add_phone(phone['value'])
                else:
                    record.add_phone(phone)
            except Exception as error:
                print(f"Phone cannot be added to record, {type(error)}, {error}, {json_dict}")
            try:
                birthday = json_dict['birthday']['value']
                record.add_birthday(birthday)
            except Exception as error:
                print(f"Birthday cannot be added to record, {type(error)}, {error}, {json_dict}")
            return record
        except Exception as error:
            print(f"Record cannot be created, {type(error)}, {error}, {json_dict}")
