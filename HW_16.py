def func_input():
    num_1 = input('Введите число 1: ')
    try:
        num_1 = int(num_1)
    except ValueError:
        print("Ошибка! Введено не число! Повторите ввод.")
        return func_input()
    num_2 = input('Введите число 2: ')
    if num_2 == '0':
        print('Второе число не может быть 0! Повтороите ввод.')
        return func_input()
    try:
        num_2 = int(num_2)
    except ValueError:
        print("Ошибка! Введено не число! Повторите ввод.")
        return func_input()
    else:
        return num_1, num_2


def main():
    n_1, n_2 = func_input()
    print(n_1/n_2)

if __name__ == '__main__':
    main()
