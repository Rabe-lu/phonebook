import pytest

from exeptions import InvalidFieldError, InvalidIndexError, InvalidContactIdError
from model.contact import Contact
from model.phonebook import PhoneBook

class TestAddContact:
    def test_add_contact(self, phonebook, test_data_contact, delete_test_contact):
        current_last_id = phonebook.last_id
        phonebook.add_contact(*test_data_contact)
        assert current_last_id + 1 == phonebook.last_id

class TestDeleteContact:
    def test_delete_contact(self, phonebook,test_contact_add):
        len_before_delete = len(phonebook.contacts)
        last_contact_id = phonebook.contacts[-1].id
        test_contact_id = phonebook.last_id
        phonebook.delete_contact(test_contact_id)
        assert len_before_delete == len(phonebook.contacts)+1
        assert last_contact_id > phonebook.contacts[-1].id

    def test_delete_incorrect_contact(self, phonebook, test_contact_add_and_delete):
        inexistent_contact_id = phonebook.contacts[-1].id + 1
        with pytest.raises(InvalidContactIdError):
            phonebook.delete_contact(inexistent_contact_id)

class TestChangeContact:
    def test_change_contact(self, phonebook, test_contact_add_and_delete):
        test_contact_id = phonebook.last_id
        test_field_to_change_number = 2
        new_value = "Измененный"

        len_before_change = len(phonebook.contacts)
        phonebook.change_contact(test_contact_id, test_field_to_change_number, new_value)
        assert test_contact_id == phonebook.last_id
        assert len_before_change == len(phonebook.contacts)

    def test_correct_changed_data(self, phonebook, test_contact_add_and_delete):
        test_contact_id = phonebook.last_id
        contact = phonebook.contacts[-1]

        old_first_name = contact.first_name
        old_last_name = contact.last_name
        old_phone = contact.phone
        old_comment = contact.comment

        test_field_to_change_number = 2
        new_value = "Измененный"

        phonebook.change_contact(test_contact_id, test_field_to_change_number, new_value)

        changed_contact = phonebook.contacts[-1]

        assert changed_contact.last_name == new_value

        assert changed_contact.last_name != old_last_name
        assert changed_contact.first_name == old_first_name
        assert changed_contact.phone == old_phone
        assert changed_contact.comment == old_comment

    def test_incorrect_index_field (self, phonebook, test_contact_add_and_delete):
        test_contact_id = phonebook.last_id
        field_to_change_number = 5
        new_value = "Невалидно"
        with pytest.raises(IndexError):
            phonebook.change_contact(test_contact_id, field_to_change_number, new_value)

    def test_incorrect_type_field (self, phonebook, test_contact_add_and_delete):
        test_contact_id = phonebook.last_id
        field_to_change_number = "Чушь"
        new_value = "Невалидно"
        with pytest.raises(TypeError):
            phonebook.change_contact(test_contact_id, field_to_change_number, new_value)

    def test_incorrect_contact_index(self, phonebook):
        test_contact_id = phonebook.contacts[-1].id + 1
        print(test_contact_id)
        field_to_change_number = 2
        new_value = "Невалидно"
        with pytest.raises(InvalidIndexError):
            phonebook.change_contact(test_contact_id, field_to_change_number, new_value)


class TestSearchContact:
    @pytest.mark.parametrize("search_value,field_name",
                             [
                                 ('Тест', 'first_name'),
                                 ('Тестовый', 'last_name'),
                                 ('+11111111','phone'),
                                 ('тестовый комментарий','comment',)

                             ])
    def test_search(self, phonebook, test_contact_add_and_delete, search_value, field_name):
        result = phonebook.search(search_value)
        found_contact = result[0]
        assert result is not None
        assert getattr(found_contact, field_name) == search_value

    def test_search_no_result(self, phonebook):
        search_value = "KRINGE"
        search_result = phonebook.search(search_value)
        assert search_result is None

    def test_search_numbers(self, phonebook):
        search_value = 123
        with pytest.raises(TypeError):
            phonebook.search(search_value)


class TestOpenFile:
    def test_open_file(self):
        error_file_name = 'inexistent_file.txt'
        with pytest.raises(FileNotFoundError):
            PhoneBook(error_file_name)







