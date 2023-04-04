import random
import string


# task 1
# total = 0
# with open('../example1.txt', 'r') as f:
#     text = f.read()
#     text.split(' ')
# for i in text:
#     if i.isdigit():
#         total += int(i)
# print(total)

# task 2
# with open('../example2.txt', 'r') as f2:
#     text2 = f2.read()
#     text2 = text2.split('\n')
#     list2int = [int(i) for i in text2 if i.isdigit()]
#     list2int.sort()
#     list2str = [i for i in text2 if i.isalpha()]
#     list2str.sort(key=len)
#     list2int += list2str
#     print(list2int)

# task 3
# with open('example3.txt', 'w') as f3:
#     str_line = input('Введите текст построчно для записи в файл, для окончания введите пустую строку: ')
#     while str_line:
#         f3.write(str_line + '\n')
#         str_line = input()

# task 4
# with open('example4.txt', 'r') as f4:
#     text4 = f4.read()
#     NumStrings = text4.count('\n') + 1
#     text4 = text4.split('\n')
#     dict4 = {f'in {i + 1} str': f'{len(x)} symbols' for i, x in zip(range(len(text4)), text4)}
#     print('Number of lines=', NumStrings, '\n', dict4)

# Home work
list_int = [random.randint(1, 99) for i in range(10)]#список из 10 рандомных чисел
list_words = list()
letters = string.ascii_lowercase
for i in range(10):
    max_len = random.randint(4, 12)#рандомно назначаем длину "слова"
    word = ''.join(random.sample(letters, max_len))#генерируем слово
    list_words.append(word)#добавляем слово в список
list_combined = list_int + list_words#объеденим списки
random.shuffle(list_combined)#перемешаем список
#список в качестве исходных данных готов

with open('hw14.txt', 'w') as file_hw14:
    list_words = list()
    list_int = list()
    for i in list_combined:
        if isinstance(i, str):
            list_words.append(i)
        elif isinstance(i, int):
            list_int.append(int(i))
    list_words.sort(key=len)
    list_int.sort()
    for i in list_words:
        file_hw14.write(i+'\n')
    for i in list_int:
        file_hw14.write(str(i)+'\n')