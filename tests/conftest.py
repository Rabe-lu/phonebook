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
def test_contact_add(phonebook,test_data_contact):
    phonebook.add_contact(*test_data_contact)

@pytest.fixture
def delete_test_contact(phonebook):
    last_id = phonebook.last_id
    yield
    phonebook.delete_contact(last_id)
