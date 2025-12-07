import json

file_name = 'contacts.json'
json_contact_fields = ['first_name', 'last_name', 'phone', 'comment']


def open_file():
    with open(file_name, 'r') as file:
        content = json.load(file)
        return content


def save_file(content):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(content, file, indent=4, ensure_ascii=False)


def show_all_contacts():
    data = open_file()
    contacts_ids = show_contacts(data['contacts'])
    return contacts_ids


def show_contacts(contacts_list):
    print('\n' + '-' * 20)
    print('Номера в вашем справочнике:')
    contacts_ids = []
    counter = 1
    for contact in contacts_list:
        contacts_ids.append(contact['id'])
        print(f'- {counter} - {contact_format(contact)}')
        counter += 1
    print('-' * 20 + '\n')
    return contacts_ids


def contact_format(contact):
    first_name = contact['first_name']
    last_name = contact['last_name']
    phone = contact['phone']
    comment = contact['comment']
    return f'{last_name} {first_name}, tel: {phone}, //{comment}//'


def add_contact(first_name: str, last_name: str, phone: str, comment: str = ""):
    data = open_file()
    new_id = data['last_id'] + 1
    new_contact = {
        'id': new_id,
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
        'comment': comment
    }

    data['contacts'].append(new_contact)
    data['last_id'] = new_id

    save_file(data)
    print('\n' + '-' * 20)
    print(f"Контакт {first_name} добавлен")
    print('-' * 20 + '\n')


def search(search_string):
    results = []
    search_string = search_string.lower()
    data = open_file()
    search_fields = json_contact_fields
    for contact in data['contacts']:
        for field in search_fields:
            if search_string in contact[field].lower():
                results.append(contact)
                break

    if not results:
        print('\n' + '-' * 20)
        print('Поиск не дал результатов')
        print('-' * 20 + '\n')
    else:
        return show_contacts(results)


def change_contact(contact_id, field_to_change_number, change_value):
    data = open_file()
    field_to_change = json_contact_fields[field_to_change_number - 1]
    for contact in data['contacts']:
        if contact['id'] == contact_id:
            contact[field_to_change] = change_value
            print(f'Успешно изменен контакт: \n'
                  f'{contact_format(contact)}')
            print('-' * 20)

    save_file(data)


def delete_contact(contact_id):
    data = open_file()
    index = -1
    for contact in data['contacts']:
        if contact['id'] == contact_id:
            index = data['contacts'].index(contact)
            break
    if index != -1:
        deleted_contact = data['contacts'][index]
        del data['contacts'][index]
        save_file(data)
        print(f'Данный контакт успешно удалён: \n'
              f'{contact_format(deleted_contact)}')
        print('-' * 20)


if __name__ == '__main__':
    command = 0
    while command != 6:
        print('Введите номер команды из списка:\n'
              '1. Показать все контакты\n'
              '2. Добавить контакт\n'
              '3. Найти контакт\n'
              '4. Изменить контакт\n'
              '5. Удалить контакт\n'
              '6. Выйти из программы'
              )

        command = int(input('\nВвод:'))
        if command == 1:
            show_all_contacts()

        elif command == 2:
            first_name, last_name, phone, comment = "", "", "", ""
            first_name = input('Введите имя:')
            last_name = input('Введите фамилию:')
            phone = input('Введите номер телефона:')
            comment = input('Введите комментарий:')
            add_contact(first_name, last_name, phone, comment)

        elif command == 3:
            search_string = input('Введите значение для поиска:')
            search(search_string)

        elif command == 4:
            command_choose = input('Введите значение для поиска контакта или "all", чтобы посмотреть все контакты. '
                                   'Для выхода в главное меню введите 0: ')
            if command_choose == 'all':
                inner_ids = show_all_contacts()
            elif command_choose == "0":
                continue
            else:
                inner_ids = search(command_choose)

            if not inner_ids:
                print('Нет доступных контактов.')
            else:
                valid_input = False
                index_to_change = None
                while not valid_input:
                    try:
                        user_input = input(
                            'Введите порядковый номер контакта для изменения. Для выхода введите 0: ')
                        index_to_change = int(user_input)
                        if index_to_change == 0:
                            print('Выход в главное меню.')
                            break
                        if 1 <= index_to_change <= len(inner_ids):
                            print(f'Выбран контакт #{index_to_change}')
                            valid_input = True
                        else:
                            print(f'Неверный номер. Допустимый диапазон: 1-{len(inner_ids)}')
                    except ValueError:
                        print(f'Ошибка: "{user_input}" не является числом. Пожалуйста, введите номер.')
                    except Exception as e:
                        print(f'Произошла непредвиденная ошибка: {e}')
                        break

                if valid_input:
                    valid_change_input = False
                    field_to_change = None
                    while not valid_change_input:
                        try:
                            user_input = input(
                                'Введите номер поля для изменения: 1 - Имя, 2 - Фамилия, 3 - Номер, 4 - Комментарий.'
                                'Введите 0 для выхода в главное меню: ')
                            field_to_change = int(user_input)
                            if field_to_change == 0:
                                print('Выход в главное меню.')
                                break
                            if 1 <= field_to_change <= 4:
                                print(f'Выбрано поле для изменения {field_to_change}')
                                valid_change_input = True
                            else:
                                print(f'Выбран неверный номер поля. Допустимый диапазон 1-4')
                        except ValueError:
                            print(f'Ошибка: "{user_input}" не является числом. Пожалуйста, введите номер.')
                        except Exception as e:
                            print(f'Произошла непредвиденная ошибка: {e}')
                            break

                    if valid_change_input:
                        new_field_data = None
                        if field_to_change == 1:
                            new_field_data = input('Введите новое имя: ')
                        elif field_to_change == 2:
                            new_field_data = input('Введите новую фамилию: ')
                        elif field_to_change == 3:
                            new_field_data = input('Введите новый номер: ')
                        elif field_to_change == 4:
                            new_field_data = input('Введите новый комментарий: ')
                        contact_id = inner_ids[index_to_change - 1]
                        change_contact(contact_id, field_to_change, new_field_data)

        elif command == 5:
            command_choose = input('Введите значение для поиска контакта или "all", чтобы посмотреть все контакты. '
                                   'Для выхода в главное меню введите 0: ')
            if command_choose == 'all':
                inner_ids = show_all_contacts()
            elif command_choose == "0":
                continue
            else:
                inner_ids = search(command_choose)

            if not inner_ids:
                print('Нет доступных контактов.')
            else:
                valid_input = False
                index_to_delete = None
                while not valid_input:
                    try:
                        user_input = input(
                            'Введите порядковый номер контакта для удаления. Для выхода введите 0: ')
                        index_to_delete = int(user_input)
                        if index_to_delete == 0:
                            print('Выход в главное меню.')
                            break
                        if 1 <= index_to_delete <= len(inner_ids):
                            print(f'Выбран контакт #{index_to_delete}')
                            valid_input = True
                        else:
                            print(f'Неверный номер. Допустимый диапазон: 1-{len(inner_ids)}')
                    except ValueError:
                        print(f'Ошибка: "{user_input}" не является числом. Пожалуйста, введите номер.')
                    except Exception as e:
                        print(f'Произошла непредвиденная ошибка: {e}')
                        break

                    if valid_input:
                        contact_id = inner_ids[index_to_delete - 1]
                        delete_contact(contact_id)
