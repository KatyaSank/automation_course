# Придумать класс и методы к нему, использовать инкапсуляцию, полиморфизм и наследование

class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.__sex = sex

    def run(self):
        return self.name + ' ' + 'runs'

    def breath(self):
        return 'breath'


class Dog(Animal):
    def voice(self):
        return self.name + ' ' + 'barks'

    def jump(self):
        return self.__sex + ' ' + 'jumps'

    def breath(self):
        return self.name + ', ' + self.age + ' ' + 'breaths'


class Cat(Animal):
    def voice(self):
        return self.name + ' ' + 'mew'



