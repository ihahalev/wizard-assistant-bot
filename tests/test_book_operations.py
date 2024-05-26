
import unittest
from datetime import datetime, timedelta

import remembrall.helpers.book_operations as sut

class TestBookOperations(unittest.TestCase):

    def setUp(self):
        self.book = sut.AddressBook()
        self.record1 = sut.Record("Dmytro")
        self.record1.add_phone("1234567890")
        self.record2 = sut.Record("Ivan")
        self.record2.add_phone("9876543210")
        self.record2.add_birthday("28.02.1988")
        self.record2.add_email("ivan@example.com")
        self.book.add_record(self.record1)
        self.book.add_record(self.record2)

    def test_add_contact(self):
        args = ["Artem", "5555555555"]
        sut.add_contact(args, self.book)
        self.assertIn("Artem", self.book.data)

    def test_change_contact(self):
        args = ["Dmytro", "Anton"]
        sut.change_contact(args, self.book)
        self.assertEqual(str(self.record1.name), "Anton")

    def test_remove_contact(self):
        args = ["Ivan"]
        sut.remove_contact(args, self.book)
        self.assertNotIn(self.record2, self.book.data.values())

    def test_change_phone(self):
        args = ["Ivan", "9876543210", "9999999999"]
        sut.change_phone(args, self.book)

        phones = [phone.value for phone in self.record2.phones]
        self.assertIn("9999999999", phones)
        self.assertNotIn("9876543210", phones)

    def test_remove_phone(self):
        args = ["Dmytro", "1234567890"]
        sut.remove_phone(args, self.book)
        self.assertTrue(len(self.record1.phones) == 0)

    def test_get_contact_phones_single(self):
        args = ["Dmytro"]
        result = sut.get_contact_phones(args, self.book)
        self.assertEqual(result, "1234567890")

    def test_get_contact_phones_multiple(self):
        args = ["Dmytro", "5555555555"]
        sut.add_contact(args, self.book)

        args = ["Dmytro"]
        result = sut.get_contact_phones(args, self.book)
        self.assertEqual(result, "1234567890; 5555555555")

    def test_get_all_contacts(self):
        result = sut.get_all_contacts(self.book)
        self.assertEqual(result,
                        "Address book:\n" \
                        "Contact name: Dmytro, phones: 1234567890, birthday: , address: , emails: \n" \
                        "Contact name: Ivan, phones: 9876543210, birthday: 28.02.1988, address: , emails: ivan@example.com"
                        )

    def test_show_contact(self):
        result = sut.show_contact(["Ivan"], self.book)
        self.assertEqual(result, "Contact name: Ivan, phones: 9876543210, birthday: 28.02.1988, address: , emails: ivan@example.com")

    def test_add_birthday(self):
        args = ["Dmytro", "01.04.1990"]
        sut.add_birthday(args, self.book)
        self.assertEqual(str(self.record1.birthday), "01.04.1990")

    def test_show_birthday(self):
        args = ["Ivan"]
        result = sut.show_birthday(args, self.book)
        self.assertEqual(str(result), "28.02.1988")

    def test_change_birthday(self):
        args = ["Ivan", "25.02.1988"]
        sut.change_birthday(args, self.book)
        self.assertEqual(str(self.record2.birthday), "25.02.1988")

    def test_get_birthdays(self):
        # set Dmytro's birthday to 2 days from now
        today = datetime.today()
        birthday = today + timedelta(days=2)
        years_old = today.year - 1995
        args = ["Dmytro", f"{birthday.day}.{birthday.month}.1995"]
        sut.add_birthday(args, self.book)

        result = sut.get_birthdays([7], self.book)
        self.assertEqual(result,
                         "Upcoming birthdays:\n" \
                         f"Dmytro's birthday is {birthday.strftime("%d.%m.%Y")}, he is {years_old} years old"
                         )

    def test_add_email(self):
        result = sut.add_email(["Dmytro", "dmytro@example.com"], self.book)
        self.assertEqual(result, "Email added")
        self.assertIn("dmytro@example.com", [str(email) for email in self.record1.emails])

    def test_change_email(self):
        result = sut.change_email(["Ivan", "ivan@example.com", "ivan.new@test.com" ], self.book)
        self.assertEqual(result, "Email changed")
        self.assertNotIn("ivan@example.com", [str(email) for email in self.record2.emails])
        self.assertIn("ivan.new@test.com", [str(email) for email in self.record2.emails])

    def test_add_address(self):
        result = sut.add_address(["Dmytro", "Kyiv Ukraine"], self.book)
        self.assertEqual(result, "Address added.")
        self.assertEqual(str(self.record1.address), "Kyiv Ukraine")

    def test_add_address_already_exists(self):
        sut.add_address(["Dmytro", "Kyiv Ukraine"], self.book)
        result = sut.add_address(["Dmytro", "Kyiv Ukraine Earth"], self.book)
        self.assertEqual(result, "Address already exists.")

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