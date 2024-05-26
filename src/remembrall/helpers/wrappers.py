import re

from .customErrors import ShortName, PhoneValidationError, DateFormatError, AddressValidationError, NoteError

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AddressValidationError as ave:
            return f"{ave}"
        except ValueError as ve:
            # get error message
            msg: str = ve.args[0]
            # if we have 'got', pattern of error will be like (expected 2, got N)
            pattern = r"got (\d)"
            msg_str = type(msg) == str
            got = ''
            if msg_str:
                got = re.search(pattern, msg)
            if got:
                is_birthday = func.__name__ == "add_birthday" or func.__name__ == "change_birthday"
                is_address = func.__name__ == "change_address" or func.__name__ == "add_address"
                is_email = func.__name__ == "change_email" or func.__name__ == "add_email"
                count = got.group(1)
                # depending on N return corresponding message
                if count == '0':
                    if is_birthday:
                        return "Give me name and birthday please."
                    if is_address:
                        return "Give me name and address please."
                    if is_email:
                        return "Give me name and email address please."
                    return "Give me name and parameters please."                
                elif count == '1':
                    if is_birthday:
                        return "Give me birthday please."
                    if is_address:
                        return "Give me address please."
                    if is_email:
                        return "Give me email address please."                   
                    return "Give me parameters please."
                elif count == '2':
                    if is_email:
                        return "Give me new email address please."
                    return "Give me new phone please."
            # if we have only expected, too many entered args
            elif msg_str and msg.find("expected") != -1:
                return "Too many arguments."
            elif func.__name__ == "get_birthdays":
                return "Please give me a number."
            # any other unexpected ValueError
            return f"{func.__name__} error, {type(ve)}, {ve}"
        except KeyError:
            return "Contact does not exist."
        except IndexError:
            if func.__name__ in ['add_address', 'change_address']:
                if len(args[0]) == 0:
                    return "Please give me name and address."
            if func.__name__ in ['add_email', 'change_email']:
                if len(args[0]) == 0:
                    return "Please give me name and email address."
            if func.__name__ in ['get_birthdays']:
                if len(args[0]) == 0:
                    return "Please give me a specified number of days."
            else:
                return "Enter user name."
        except ShortName as name:
            return f"{name}"
        except PhoneValidationError as phone:
            return f"{phone}"
        except DateFormatError as format:
            return f"{format}"
        except Exception as error:
            return f"{func.__name__} error, {type(error)}, {error}"
    return inner

def file_read_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as error:
            print(f"File {error.filename} not found.")
        except Exception as error:
            print(f"File could not be read, {type(error)}, {error}")
    return inner

def note_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NoteError as ne:
            return f"{ne}"
        except IndexError:
            if func.__name__ == 'change_note' and len(args[0]) < 2:
                return "Please give a note title and new content text."
            if func.__name__ in ['add_note', 'show_note', 'remove_note']:
                if len(args[0]) == 0:
                    return "Please give a note title."
                return "Please give a content text."
        except ValueError:
            if func.__name__ == 'change_note_title' and len(args[0]) < 2:
                return "Please give a note title and new title."
            if func.__name__ == 'add_note_tag' and len(args[0]) < 2:
                return "Please give a note title and tag."
            if func.__name__ == 'remove_note_tag' and len(args[0]) < 2:
                return "Please give a note title and tag."
            return "Please give required arguments."
        except Exception as error:
            return f"{func.__name__} error, {type(error)}, {error}"
    return inner
