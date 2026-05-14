from exeptions import InvalidIndexError
from .file_reader import FileReader
from .file_writer import FileWriter
from .contact import Contact


class PhoneBook:
    def __init__(self, file_name):
        self.file_name = file_name
        self.reader = FileReader(file_name)
        self.writer = FileWriter(file_name)
        self.contacts = []
        self.last_id = 0
        self.load_contacts()

    def load_contacts(self):
        data = self.reader.open_file()
        self.last_id = data.get('last_id', 0)
        self.contacts = [Contact.from_dict(c) for c in data.get('contacts', [])]

    def add_contact(self, first_name: str, last_name: str, phone: str, comment: str = ""):
        new_id = self.last_id + 1
        new_contact = Contact(new_id, first_name, last_name, phone, comment)
        self.contacts.append(new_contact)
        self.last_id = new_id

        data_to_save = {
            "contacts": [c.to_dict() for c in self.contacts],
            "last_id": self.last_id
        }
        self.writer.save_file(data_to_save)

        print('\n' + '-' * 20)
        print(f"Добавлен контакт: {new_contact.contact_format()}")
        print('-' * 20 + '\n')

    def search(self, search_string: str):
        search_string = search_string.lower()
        result = []
        for contact in self.contacts:
            fields = [contact.first_name, contact.last_name, contact.phone, contact.comment]
            if any(search_string in field.lower() for field in fields):
                result.append(contact)
        if not result:
            print('\n' + '-' * 20)
            print('(｡•́︿•̀｡) Поиск не дал результатов')
            print('-' * 20 + '\n')
        else:
            return result

    def change_contact(self, contact_id, field_to_change_number, change_value):
        field_to_change = Contact.fields[field_to_change_number - 1]
        is_contact_id_exist = False
        for contact in self.contacts:
            if contact.id == contact_id:
                setattr(contact, field_to_change, change_value)
                is_contact_id_exist = True
                break

        if not is_contact_id_exist:
            raise InvalidIndexError

        data_to_save = {
            "contacts": [c.to_dict() for c in self.contacts],
            "last_id": self.last_id
        }

        self.writer.save_file(data_to_save)
        print('-' * 20)
        print(f'Успешно изменен контакт: \n'
              f'{contact.contact_format()}')
        print('-' * 20)

    def delete_contact(self, contact_id):
        for i, contact in enumerate(self.contacts):
            if contact.id == contact_id:
                del self.contacts[i]

                data_to_save = {
                    "contacts": [c.to_dict() for c in self.contacts],
                    "last_id": self.last_id
                }

                self.writer.save_file(data_to_save)
                print(f'Успешно удален контакт: \n'
                      f'{contact.contact_format()}')
                print('-' * 20)
