# my_dict = {'a': 1, 'b': 2, 'c': 3}
# try:
#     value = my_dict['a']
# except KeyError:
#     print('Произошла ошибка KeyError')
# else:
#     print('Ошибок не произошло')
# finally:
#     print('Оператор finally выполнен!')
# task 3
# num_1 = int(input('Введите число 1: '))
# num_2 = int(input('Введите число 2: '))
# try:
#     result = num_1 / num_2
# except ZeroDivisionError:
#     print('Ошибка деления на 0')
# else:
#     print(result**2)
# finally:
#     print('Finally существует!')
# task 4
# try:
#     num1 = int(input('Number 1: '))
#     num2 = int(input('Number 2: '))
#     result = num1 / num2
# except ZeroDivisionError:
#     print('Деление на 0')
# except ValueError:
#     print('Введены не числа')
# except Exception:
#     print('Другая ошибка')
# else:
#     print(result)

import csv
import json
def read_file(file_name):
    try:
        if file_name.endswith('.csv'):
            file = open(file_name, 'r', encoding='UTF-8')
            data = list(csv.reader(file))
        elif file_name.endswith('.json'):
            file = open(file_name, 'r', encoding='UTF-8')
            data = dict(json.load(file))
    except FileNotFoundError:
        print('файл не найден')
    except IsADirectoryError:
        print('это не файл, а директория')
    else:
        file.close()
        return data
def write_to_file(file_name, data):
    try:
        if file_name.endswith('.csv'):
            file = open(file_name, 'w', encoding='UTF-8')
            csvWriter = csv.writer(file)
            for row in data:
                csvWriter.writerow(row)
        elif file_name.endswith('.json'):
            file = open(file_name, 'w', encoding='UTF-8')
            json.dump(data, file)
    except FileExistsError:
        print('Файл с таким именем уже существует')
def main():
    file_name_read = input('Какой файл читаем: ')
    file_name_write = input('В какой файл запишем: ')
    content = read_file(file_name_read)
    write_to_file(file_name_write, content)

if __name__ == '__main__':
    main()
