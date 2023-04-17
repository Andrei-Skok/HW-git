import string
from random import randint


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print_(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__(lang='En', letters=string.ascii_uppercase)
        self.__letters_num = len(self.letters)

    def is_en_letter(self, letter):
        return letter.upper() in string.ascii_uppercase

    def letters_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return 'This is example text in English'


primer = EngAlphabet()
print(primer.letters_num())
print(primer.is_en_letter('F'))
print(primer.is_en_letter('Ш'))
print(primer.example())

print('==========================')


class Tomato:
    # стадии созревания помидора
    states = {1: 'green', 2: 'yellow', 3: 'orange', 4: 'red'}

    # создаем помидор с индексом и присваиваем ему 1ую стадию созревания - зеленый
    def __init__(self, index):
        self._index = index
        self._states = Tomato.states[1]

    # метод роста помидора
    def grow(self):
        for item in Tomato.states.items():  # определяем стадию созревания экземпляра класса
            if self._states in item:
                stage_ripening = item[0]
        if not self.is_ripe():  # если еще не спелый (красный) переводим на следующую стадию
            stage_ripening += 1
        self._states = Tomato.states[stage_ripening]

    # метод созрел ли томат
    def is_ripe(self):
        return self._states == 'red'


class TomatoBush:
    # создаем куст с количеством помидоров
    def __init__(self, num_tomatoes):
        self.num_tomatoes = num_tomatoes
        self.tomatoes = [Tomato(index) for index in range(num_tomatoes)]  # список помидоров

    # метод роста всех томатов на кусте
    def grow_all(self):
        # map(lambda tomato: tomato.grow(), self.tomatoes) #так нельзя??
        for tomato in self.tomatoes:
            tomato.grow()

    # метод возвращает True если все томаты на кусте стали спелыми
    def all_are_ripe(self):
        for tomato in self.tomatoes:
            if tomato._states in ['green', 'yellow', 'orange']:
                all_are_ripe = False
                break
        else:
            all_are_ripe = True
        return all_are_ripe

    # метод чистит список томатов на кусте
    def give_away_all(self):
        self.tomatoes.clear()

    # метод показывает текущее состояние помидоров на кусте
    def info(self):
        for tomato in self.tomatoes:
            print(f'Tomato #{tomato._index} is {tomato._states}')


class Gardener:
    # создаем огородника с именем и передаем ему куст
    def __init__(self, name, _plant):
        self.name = name
        self._plant = _plant

    # метод огородника работать - рандомно зреет или один рандомный помидор, или весь куст
    def work(self):
        print(f'{self.name} worked hard!')
        grow_one_tomato_or_all_bush = randint(0, 1)
        if grow_one_tomato_or_all_bush:
            index = randint(0, self._plant.num_tomatoes - 1)
            print(index)
            self._plant.tomatoes[index].grow()
            print(f'Only one tomato turned {self._plant.tomatoes[index]._states}')
        else:
            self._plant.grow_all()
            print('All the tomatoes on the bush have become more mature')

    # метод сборки урожая если все помидоры спелые - чистим куст
    def harvest(self):
        if self._plant.all_are_ripe():
            print('Hooray, the harvest is in!!!')
            self._plant.give_away_all()
        else:
            print('Not all tomatoes are ripe yet((')

    # метод показывает справку по садаводству
    @staticmethod
    def knowledge_base():
        print('Если высадить томаты в открытый грунт очень рано,\n'
              'то увеличивается риск гибели рассады из-за низких \n'
              'температур в ночное время')


# Тесты
# Gardener.knowledge_base()

bush_1 = TomatoBush(6)

gardener_1 = Gardener('Andrei', bush_1)

gardener_1.work()
print(bush_1.all_are_ripe())
gardener_1.work()
print(bush_1.all_are_ripe())
gardener_1.work()
print(bush_1.all_are_ripe())

gardener_1.harvest()
bush_1.info()

for i in range(3):
    gardener_1.work()

bush_1.info()
gardener_1.harvest()
