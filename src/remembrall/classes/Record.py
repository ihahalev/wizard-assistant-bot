from classes import Name, Phone, Birthday, Email
from .customErrors import PhoneValidationError, EmailValidationError
from helpers.wrappers import input_error
from helpers.json_converter import to_json

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday = None
        self.emails: list[Email] = []       

    def __str__(self):
        name = f"name: {self.name.value}"
        phones = f"phones: {'; '.join(p.value for p in self.phones if p.value)}"
        birthday = f"birthday: {self.birthday if self.birthday else ''}"
        emails = f"emails: {'; '.join(e.value for e in self.emails if e.value)}"

        return f"Contact {name}, {phones}, {birthday}, {emails}"

    @input_error
    def add_phone(self, phone_number: str):
        if not [phone for phone in self.phones if phone.value == phone_number]:
            self.phones.append(Phone(phone_number))

    def add_email(self, user_email: str):
        email = self.find_email(user_email)
        if email:
            print( "Email exists")
            return
        valid_email = Email(user_email)
        self.emails.append(valid_email)

    def remove_email(self, rem_email):
        self.emails = [e for e in self.emails if e.value != rem_email]

    def find_phone(self, phone_number:str) -> Phone:
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
            
    def find_email(self, find_email: str) -> Email:
        for e in self.emails:
            if find_email == e.value:
                return e

    def edit_phone(self, old_phone:str, new_phone:str):
        found_phone = self.find_phone(old_phone)
        if not found_phone:
            raise PhoneValidationError("Phone number not found")
        found_phone.edit_phone(new_phone)

    def edit_email(self, find_e: str, replace_e: str):
        email = self.find_email(find_e)
        if not email:
            # print( "Email not found")
            raise EmailValidationError("Email address not found")
        email.value = Email(replace_e).value

    def add_birthday(self, birthday):
        if not self.birthday:
            self.birthday = Birthday(birthday)

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
                emails = json_dict['emails']
                if type(emails) is list:
                    for email in emails:
                        record.add_email(email['value'])
                else:
                    record.add_email(email)
            except Exception as error:
                print(f"Email address cannot be added to record, {type(error)}, {error}, {json_dict}")
            try:
                birthday = json_dict['birthday']['value']
                record.add_birthday(birthday)
            except Exception as error:
                print(f"Birthday cannot be added to record, {type(error)}, {error}, {json_dict}")
            return record
        except Exception as error:
            print(f"Record cannot be created, {type(error)}, {error}, {json_dict}")
