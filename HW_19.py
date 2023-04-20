def decorator(func):
    def wrapper(arg, **kwargs):
        new_list = list()
        for sub_list in arg:
            for i in sub_list:
                if i % 3 != 0:
                    new_list.append(i)
        result = func(arg)
        print(len(new_list))
        return result

    return wrapper


@decorator
def foo(arg):
    new_list = list()
    for sub_list in arg:
        for i in sub_list:
            if i % 3 == 0:
                new_list.append(i)
    return new_list


list_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(foo(list_))

print('Home work 19 =============================================')


def debug(func):
    def wrapper(*args):
        print(f'was called function {func.__name__} with parametres {args}')
        result = func(*args)
        print(f'result of fuction = {result}')
        return result

    return wrapper


@debug
def multy(a, b):
    return a * b


multy(2, 7)
multy(3, 7)
multy(4, 7)
multy(5, 7)
