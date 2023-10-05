from scripts import create_file, show_contacts, write_file, get_info, change_contact, delete_contact
from os.path import exists


def ui():
    if not exists('Phone_book.csv'):
         create_file()

    print(f'Добро пожаловать в телефонную книгу!\n')
    
    while True:
        print(f'\nВыбирите желаемое действие:\n\n\
1 - Показать список контактов\n2 - Записать контакт\n3 - Изменить контакт\n4 - Удалить контакт\n\
5 - выйти из программы')  
        try:
            command = int(input('\nВведите команду: ')) 
        except ValueError:
            command = 0

        if command == 0 or command > 6:
            print('\nВы ввели неверный номер команды!\n')
        elif command == 1:
            show_contacts('Phone_book.csv')
        elif command == 2:
            write_file('Phone_book.csv', get_info())
        elif command == 3:
            change_contact('Phone_book.csv')
        elif command == 4:
            delete_contact('Phone_book.csv')
        elif command == 5:
            print('Спасибо, что воспользовались нашей программой!')
            break
ui()

