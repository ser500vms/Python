import csv


def create_file():
    with open('Phone_book.csv', "w", encoding="utf-8") as data:
        f_writer = csv.DictWriter(data, fieldnames=['№', 'Фамилия', 'Имя', 'Отчество', 'Номер телефона'])
        f_writer.writeheader()

def get_info():
    with open('Phone_book.csv', encoding="utf-8") as data:
        f_reader = list(csv.reader(data))
        row_count = len(f_reader) - 1 
    number = str(row_count)
    family = 'Zavyalov'
    name = 'Sergey'
    surname = 'Vital'
    phone = '8-900-301-12-13'
    info = [number, family, name, surname, phone]
    return info

def show_contacts(file_name):
    with open(file_name, encoding="utf-8") as data:
        f_reader = csv.DictReader(data)
        result = list(f_reader)
        print(result)
    return result

def write_file(file_name, lst):
    with open(file_name, encoding="utf-8") as data:
        f_reader = csv.DictReader(data)
        result = list(f_reader)
    obj = {'№': lst[0], 'Фамилия': lst[1], 'Имя': lst[2], 'Отчество': lst[3], 'Номер телефона': lst[4]}
    result.append(obj)
    with open('Phone_book.csv', "w", encoding="utf-8", newline='') as data:
        f_writer = csv.DictWriter(data, fieldnames=['№', 'Фамилия', 'Имя', 'Отчество', 'Номер телефона'])
        f_writer.writeheader()
        f_writer.writerows(result)


def change_contact(file_name):
    row_to_change = int(input('Введите номер записи для изменения: ')) - 1
    changed_row = get_info()
    with open(file_name, encoding="utf-8") as data:
        f_reader = csv.DictReader(data)
        result = list(f_reader)
    obj = {'№': str(row_to_change + 1), 'Фамилия': changed_row[1], 'Имя': changed_row[2], 'Отчество': changed_row[3], 'Номер телефона': changed_row[4]}
    result[row_to_change] = obj
    with open('Phone_book.csv', "w", encoding="utf-8", newline='') as data:
        f_writer = csv.DictWriter(data, fieldnames=['№', 'Фамилия', 'Имя', 'Отчество', 'Номер телефона'])
        f_writer.writeheader()
        f_writer.writerows(result)

def delete_contact(file_name):
    row_to_delete = int(int(input('Введите номер записи для удаления: ')) - 1)
    with open(file_name, encoding="utf-8") as data:
        f_reader = csv.DictReader(data)
        result = list(f_reader)
        result.pop(row_to_delete)
        number_contact = 1
        for row in result:
            row['№'] = number_contact
            number_contact += 1
    with open('Phone_book.csv', "w", encoding="utf-8", newline='') as data:
        f_writer = csv.DictWriter(data, fieldnames=['№', 'Фамилия', 'Имя', 'Отчество', 'Номер телефона'])
        f_writer.writeheader()
        f_writer.writerows(result)   




