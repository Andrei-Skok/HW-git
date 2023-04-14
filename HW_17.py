class STR_or_INT:
    def __init__(self, obj):
        self.obj = obj
    def method(self):
        if isinstance(self.obj, str):
            counter_vowels = 0
            counter_consonats = 0
            vowels = 'eyuioa'
            consonats = 'qwrtpsdfghjklzxcvbnm'
            self.obj = self.obj.lower()
            for symbol in self.obj:
                if symbol in vowels:
                    counter_vowels += 1
                elif symbol in consonats:
                    counter_consonats += 1
            if counter_consonats * counter_vowels <= len(self.obj):
                for symbol in self.obj:
                    if symbol in vowels: print(symbol, end=' ')
            else:
                for symbol in self.obj:
                    if symbol in consonats: print(symbol, end=' ')
        elif isinstance(self.obj, int):
            sum_even = 0
            for digit in str(self.obj):
                if int(digit) % 2 == 0:
                    sum_even += int(digit)
            print(sum_even*len(str(self.obj)))


instance_1 = STR_or_INT('This is example string')
instance_1.method()
print('\n', '============================')
instance_2 = STR_or_INT(2520)
instance_2.method()
