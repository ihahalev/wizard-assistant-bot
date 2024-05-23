
import unittest
from datetime import datetime, timedelta
from remembrall.helpers.book_operations import *

class TestBookOperations(unittest.TestCase):

    def setUp(self):
        self.book = AddressBook()
        self.record1 = Record("Dmytro")
        self.record1.add_phone("1234567890")
        self.record2 = Record("Ivan")
        self.record2.add_phone("9876543210")
        self.record2.add_birthday("28.02.1988")
        self.book.add_record(self.record1)
        self.book.add_record(self.record2)

    def test_add_contact(self):
        args = ["Artem", "5555555555"]
        add_contact(args, self.book)
        self.assertIn("Artem", self.book.data)

    def test_change_contact(self):
        args = ["Dmytro", "Anton"]
        change_contact(args, self.book)
        self.assertEqual(str(self.record1.name), "Anton")

    def test_remove_contact(self):
        args = ["Ivan"]
        remove_contact(args, self.book)
        self.assertNotIn(self.record2, self.book.data.values())

    def test_change_phone(self):
        args = ["Ivan", "9876543210", "9999999999"]
        change_phone(args, self.book)

        phones = [phone.value for phone in self.record2.phones]
        self.assertIn("9999999999", phones)
        self.assertNotIn("9876543210", phones)

    def test_remove_phone(self):
        args = ["Dmytro", "1234567890"]
        remove_phone(args, self.book)
        self.assertTrue(len(self.record1.phones) == 0)

    def test_get_contact_phones_single(self):
        args = ["Dmytro"]
        result = get_contact_phones(args, self.book)
        self.assertEqual(result, "1234567890")

    def test_get_contact_phones_multiple(self):
        args = ["Dmytro", "5555555555"]
        add_contact(args, self.book)

        args = ["Dmytro"]
        result = get_contact_phones(args, self.book)
        self.assertEqual(result, "1234567890; 5555555555")

    def test_get_all_contacts(self):
        result = get_all_contacts(self.book)
        self.assertEqual(result,
                        "Address book:\n" \
                        "Contact name: Dmytro, phones: 1234567890, birthday: \n" \
                        "Contact name: Ivan, phones: 9876543210, birthday: 28.02.1988"
                        )

    def test_add_birthday(self):
        args = ["Dmytro", "01.04.1990"]
        add_birthday(args, self.book)
        self.assertEqual(str(self.record1.birthday), "01.04.1990")

    def test_show_birthday(self):
        args = ["Ivan"]
        result = show_birthday(args, self.book)
        self.assertEqual(str(result), "28.02.1988")

    def test_change_birthday(self):
        args = ["Ivan", "25.02.1988"]
        change_birthday(args, self.book)
        self.assertEqual(str(self.record2.birthday), "25.02.1988")

    def test_get_birthdays(self):
        # set Dmytro's birthday to 2 days from now
        today = datetime.today()

        weekday = today.weekday()
        # make sure birthday is not on weekend for this test
        if weekday in [4,5]: # move to Monday
            birthday = today + timedelta(days=7-weekday)
        else: # move to next day
            birthday = today + timedelta(days=1)

        args = ["Dmytro", f"{birthday.day}.{birthday.month}.1995"]
        add_birthday(args, self.book)

        result = get_birthdays([7], self.book)
        self.assertEqual(result,
                         "Upcoming birthdays:\n" \
                         f"{{'name': 'Dmytro', 'congratulation_date': '{birthday.strftime("%d.%m.%Y")}'}}"
                         )

    def test_add_email(self):
        pass

    def test_change_email(self):
        pass

    def test_add_address(self):
        pass

    def test_change_address(self):
        pass

    def test_add_note(self):
        pass

    def test_show_note(self):
        pass

    def test_change_note(self):
        pass

    def test_remove_note(self):
        pass

    def test_change_note_title(self):
        pass

    def test_add_note_tag(self):
        pass

    def test_change_note_tag(self):
        pass

    def test_remove_note_tag(self):
        pass

if __name__ == '__main__':
    unittest.main()