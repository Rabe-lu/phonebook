import json

file_name = 'contacts.json'


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
        first_name = contact['first_name']
        last_name = contact['last_name']
        phone = contact['phone']
        comment = contact['comment']
        print(f'- {counter} - {last_name} {first_name}, tel: {phone}, //{comment}//')
        counter += 1
    print('-' * 20 + '\n')
    return contacts_ids


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
    search_fields = ['first_name', 'last_name', 'phone', 'comment']
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
        show_contacts(results)


def change_contact(contact_id, field_to_change, change_value):
    data = open_file()
    for contact in data['contacts']:
        if contact['id'] == contact_id:
            contact[field_to_change] = change_value
            print('Успешно изменено:')
            show_contacts([contact])
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
        del data['contacts'][index]
        save_file(data)
        print('Успешно удалено!')
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
            command_choose = input('Введите значение для поиска контакта или "all", чтобы посмотреть все контакты')
            if command_choose == 'all':
                inner_ids = show_all_contacts()
                index_to_change = input('Введите порядковый номер контакта для изменения:')
                while index_to_change > len(inner_ids) and index_to_change <= 0:
                    print('Неверный номер')
                    field_to_change = input(
                        'Введите номер поля для изменения: 1 - Имя, 2 - Фамилия, 3 - Номер, 4 - Комментарий ')
                change_value = input('Новое значение:')
