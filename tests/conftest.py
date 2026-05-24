import pytest
from model.phonebook import PhoneBook


@pytest.fixture
def phonebook():
    return PhoneBook('contacts.json')
@pytest.fixture
def test_data_contact():
    data = ["Тест", "Тестовый", "+11111111", "тестовый комментарий"]
    return data


@pytest.fixture
def test_contact_add_and_delete(phonebook,test_data_contact):
    phonebook.add_contact(*test_data_contact)
    created_contact = phonebook.contacts[-1]
    yield created_contact
    phonebook.delete_contact(created_contact.id)
#

@pytest.fixture
def test_contact_add(phonebook,test_data_contact):
    phonebook.add_contact(*test_data_contact)

@pytest.fixture
def delete_test_contact(phonebook):
    yield
    last_id = phonebook.last_id
    phonebook.delete_contact(last_id)
