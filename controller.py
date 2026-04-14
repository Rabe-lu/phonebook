from model.phonebook import PhoneBook
from view import show_all_contacts, show_contacts
from exeptions import InvalidIndexError, InvalidFieldError

pb = PhoneBook('contacts.json')


def run():
    command = 0
    while command != 6:
        try:
            print('Введите номер команды из списка:\n'
                  '1. Показать все контакты\n'
                  '2. Добавить контакт\n'
                  '3. Найти контакт\n'
                  '4. Изменить контакт\n'
                  '5. Удалить контакт\n'
                  '6. Выйти из программы'
                  )

            command = int(input('\nВвод: '))
            if command == 1:
                show_all_contacts(pb.contacts)

            elif command == 2:
                last_name = input('Введите фамилию: ')
                first_name = input('Введите имя: ')
                phone = input('Введите номер телефона: ')
                comment = input('Введите комментарий: ')
                pb.add_contact(first_name, last_name, phone, comment)

            elif command == 3:
                search_string = None
                while search_string != "exit":
                    search_string = input('Введите значение для поиска. Для выхода в главное меню введите "exit": ')
                    result = pb.search(search_string)
                    if result:
                        show_contacts(result)


            elif command == 4:
                command_choose = input(
                    'Введите значение для поиска контакта или "all", чтобы посмотреть все контакты. '
                    'Для выхода в главное меню введите "exit": ')
                if command_choose == "exit":
                    continue
                elif command_choose == 'all':
                    result = pb.contacts
                    show_all_contacts(result)
                    inner_ids = [contact.id for contact in result]
                else:
                    result = pb.search(command_choose)
                    if not result:
                        inner_ids = None
                        continue
                    else:
                        show_contacts(result)
                        inner_ids = [contact.id for contact in result]

                try:
                    index_to_change = int(input('Введите индекс контакта для изменения: '))
                    if index_to_change > len(inner_ids):
                        raise InvalidIndexError
                    contact_id = inner_ids[index_to_change - 1]

                except InvalidIndexError:
                    print("\n(｡•́︿•̀｡) Нет такого контакта!\n")
                    continue

                try:
                    field_to_change = int(input('Введите номер поля для изменения:\n'
                                                '1. Фамилия\n'
                                                '2. Имя\n'
                                                '3. Номер телефона\n'
                                                '4. Комментарий\n: '))
                    if field_to_change > 4:
                        raise InvalidFieldError
                    new_field_data = input('Введите новое значение: ')
                    pb.change_contact(contact_id, field_to_change, new_field_data)
                except InvalidFieldError:
                    print("\n(｡•́︿•̀｡) Нет такого поля для редактирования!\n")
                    continue
                except ValueError:
                    print("\n(｡•́︿•̀｡) Нет такого поля для редактирования!\n")
                    continue

            elif command == 5:
                command_choose = input('Введите значение для поиска контакта или "all", чтобы посмотреть все контакты. '
                                       'Для выхода в главное меню введите "exit": ')
                if command_choose == "exit":
                    continue

                elif command_choose == 'all':
                    all_contacts = pb.contacts
                    show_all_contacts(all_contacts)
                    inner_ids = [contact.id for contact in all_contacts]

                else:
                    result = pb.search(command_choose)
                    if not result:
                        inner_ids = None
                        continue
                    else:
                        show_contacts(result)
                        inner_ids = [contact.id for contact in result]
                try:
                    index_to_delete = int(input('Введите порядковый номер контакта: '))
                    if index_to_delete > len(inner_ids):
                        raise InvalidIndexError

                    inner_id_to_delete = inner_ids[index_to_delete - 1]
                    pb.delete_contact(inner_id_to_delete)

                except InvalidIndexError:
                    print("\n(｡•́︿•̀｡) Нет такого контакта!\n")
                    continue
                except ValueError:
                    print("\n(｡•́︿•̀｡) Некорректное значение! !\n")
                    continue

        except ValueError:
            print("\n" + "!" * 20)
            print("Некорректное значение!\nВведите номер доступной команды")
            print("!" * 20 + "\n")
            continue
