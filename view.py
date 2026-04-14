def show_contacts(result):
    print('\n' + '-' * 20)
    print('Номера в вашем справочнике:')
    for index, contact in enumerate(result, start=1):
        print(f'- {index} - {contact.contact_format()}')
    print('-' * 20 + '\n')
    return contact


def show_all_contacts(contacts):
    if not contacts:
        print("\n" + "-" * 20)
        print("Справочник пуст")
        print("-" * 20 + "\n")
        return

    print("\n" + "-" * 20)
    print("Список контактов:")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact.contact_format()}")
    print("-" * 20 + "\n")
