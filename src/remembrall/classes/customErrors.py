# NOTE: We shjould get rid of this file and
# move exceptions to helpers folder to avoid circular imports

class ShortName(Exception):
    pass

class PhoneValidationError(Exception):
    pass

class DateFormatError(Exception):
    pass

class AddressValidationError(ValueError):
    pass

class NoteError(Exception):
    pass
