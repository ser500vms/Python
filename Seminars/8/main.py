from csv import DictReader, DictWriter
from os.path import exists

def crate_file():
    with open('Phone.csv', "w", encoding="utf-8") as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()

def get_info():
    info = ['Ivaniv', 'Ivan', '8-903-111-11-11']
    return info

def read_file(file_name):
    with open(file_name, encoding="utf-8") as data:
        f_reader = DictReader(data)
        result = list(f_reader)
    return result

def write_file(file_name, lst):
    with open(file_name, encoding="utf-8") as data:
        f_reader = DictReader(data)
        result = list(f_reader)
    obj = {"Фамилия": lst[0], "Имя": lst[1], "Номер": lst[2]}
    result.append(obj)
    with open('Phone.csv', "w", encoding="utf-8", newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        f_writer.writerows(result)

def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('Phone.csv'):
                break
            print(read_file('Phone.csv'))
        elif command == 'w':
            if not exists('Phone.csv'):
                crate_file()
            write_file('Phone.csv', get_info())

main()