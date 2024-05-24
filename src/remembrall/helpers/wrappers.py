import re

from .customErrors import ShortName, PhoneValidationError, DateFormatError, AddressValidationError, NoteError

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AddressValidationError as ave:
            return f"{ave}"
        except NoteError as ne:
            return f"{ne}"
        except ValueError as ve:
            # get error message
            msg: str = ve.args[0]
            # if we have 'got', pattern of error will be like (expected 2, got N)
            pattern = r"got (\d)"
            got = re.search(pattern, msg)
            if got:
                is_birthday = func.__name__ == "add_birthday"
                is_address = func.__name__ == "change_address" or func.__name__ == "add_address"
                count = got.group(1)
                # depending on N return corresponding message
                if count == '0':
                    if is_birthday:
                        return "Give me name and birthday please."
                    return "Give me name and phone please."
                elif count == '1':
                    if is_birthday:
                        return "Give me birthday please."
                    if is_address:
                        return "Give me address please."
                    return "Give me phone please."
                elif count == '2':
                    return "Give me new phone please."
            # if we have only expected, too many entered args
            elif msg.find("expected") != -1:
                return "Too many arguments."
            # any other unexpected ValueError
            func_names = ['add_note', 'show_note', 'change_note', 'remove_note', 'change_note_title', 'add_note_tag', 'change_note_tag', 'remove_note_tag']
            if func.__name__ in func_names:
                return "Invalid value provided."
            return f"{func.__name__} error, {type(ve)}, {ve}"
        except KeyError:
            return "Contact does not exist."
        except IndexError:
            if func.__name__ in ['add_address', 'change_address']:
                if len(args[0]) == 0:
                    return "Please give me name and address."
            if func.__name__ == 'find_notes_with_tag':
                if len(args[0]) == 0:
                    return "Please give me tag."
            if func.__name__ == 'find_notes_with_content':
                if len(args[0]) == 0:
                    return "Please give me content."
            if func.__name__ in ['show_note', 'remove_note', 'change_note_title', 'add_note_tag', 'change_note_tag', 'remove_note_tag', 'add_note', 'change_note',]:
                if len(args[0]) == 0:
                    return "Please give me title."
            if func.__name__ in ['change_note', 'add_note']:
                if len(args[0]) == 1:
                    return "Please give me content."
            if func.__name__ == 'change_note_title':
                if len(args[0]) == 1:
                    return "Please give me new title."
            if func.__name__ in ['add_note_tag', 'change_note_tag', 'remove_note_tag']:
                if len(args[0]) == 1:
                    return "Please give me tag."
            if func.__name__ == 'change_note_tag':
                if len(args[0]) == 2:
                    return "Please give me new tag." 
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
