# Цветочница.
# Определить иерархию и создать несколько цветов. Собрать букет с использованием аксессуаров с определением его стоимости.
# Определить время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов стоимости
# Узнать, есть ли цветок в букете.

class Flower:
    def __init__(self, cost, time, name):
        self.cost = cost
        self.time = time
        self.name = name


class Tulip(Flower):
    def __init__(self, cost, time, name, red=None):
        super().__init__(cost, time, name)
        self.color = red


class Orchid(Flower):
    def __init__(self, cost, time, name, vanda=None):
        super().__init__(cost, time, name)
        self.subspecies = vanda


class Magnolia(Flower):
    def __init__(self, cost, time, name):
        super().__init__(cost, time, name)
        self.high = 20


class Buket:
    def __init__(self, list_of_flowers):
        self.list_of_flowers = list_of_flowers
        self.cost = 0
        self.time_of_living = 0
        self.sorting = 0

    def cost_of_buket(self):
        for flower in self.list_of_flowers:
            self.cost += flower.cost
        return f'Cost of the buket is {self.cost}.'

    def lifecycle(self):
        for flower in self.list_of_flowers:
            self.time_of_living += flower.time
        return f'Average fade time is  {self.time_of_living / len(self.list_of_flowers)}.'

    def sorting_by_cost(self):
        self.sorting = sorted(self.list_of_flowers, key=lambda x: x.cost)
        for flower in self.sorting:
            print(flower.name)

    def including_flowers(self):
        for flower in self.list_of_flowers:
            print(f'{flower.name} is in the buket.')
