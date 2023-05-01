def func_div_3(arg):
    for _ in arg:
        if _ % 3 == 0:
            yield _


example_1 = func_div_3([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(next(example_1))
print(next(example_1))
print(next(example_1))


class EverySecondSymbol:
    def __init__(self, string_in):
        self.string_in = string_in

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.string_in):
            raise StopIteration
        symbol = self.string_in[self.index]
        self.index += 2
        return symbol


example_2 = EverySecondSymbol('qwertyuiop')
for i in example_2:
    print(i)


def intersection(list_1, list_2):
    for elem in list_1:
        if elem in list_2:
            yield elem


l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [7, 3, 21, 23, 34, 45, 67]
example_3 = intersection(l1, l2)

for _ in example_3:
    print(_)


def string_with_a(arg):
    for every_str in arg:
        if 'a' in every_str:
            yield every_str


l3 = ['hello', 'python', 'function', 'last', 'luck', 'original']

example_4 = string_with_a(l3)
for _ in example_4:
    print(_)


class EveryThird:
    def __init__(self, numbers):
        self.numbers = numbers

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        number = self.numbers[self.index]
        self.index += 3
        return number


l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
example_5 = EveryThird(l4)
for _ in example_5:
    print(_)


class CardDeck:

    def __init__(self):
        suits = ['Крести', 'Черви', 'Пик', 'Бубна']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
        self.deck = set()
        for suit in suits:
            for value in values:
                self.deck.add(value + ' ' + suit)

    def __iter__(self):
        return self

    def __next__(self):
        if self.deck:
            return self.deck.pop()
        raise StopIteration


first_deck = CardDeck()

for card in first_deck:
    print(card)
