from dataclasses import dataclass


# Цветочница.
# Определить иерархию и создать несколько цветов. Собрать букет с использованием аксессуаров с определением его стоимости.
# Определить время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов стоимости
# Узнать, есть ли цветок в букете.


class Flower:
    def __init__(self, cost, time):
        self.cost = cost
        self.time = time


@dataclass
class Tulip(Flower):
    name: str = "Tulip"
    cost: int = 8
    time: int = 10


@dataclass
class Orchid(Flower):
    name: str = "Orchid"
    cost: int = 7
    time: int = 2


@dataclass
class Magnolia(Flower):
    name: str = "Magnolia"
    cost: int = 12
    time: int = 10


class Buket:
    @staticmethod
    def create_buket():
        global a
        a = list()
        a.append(tulip.name)
        a.append(orchid.name)
        a.append(orchid.name)
        a.append(magnolia.name)
        print("My buket consists of - " + str(a))

        def cost_of_buket():
            cost = 0
            for x in a:
                if x == tulip.name:
                    cost += tulip.cost
                if x == orchid.name:
                    cost += orchid.cost
                if x == magnolia.name:
                    cost += magnolia.cost
            print("Cost of buket is " + str(cost))

        cost_of_buket()

    @staticmethod
    def lifecycle():
        total_time = 0
        for y in a:
            if y == tulip.name:
                total_time += tulip.time
            if y == orchid.name:
                total_time += orchid.time
            if y == magnolia.name:
                total_time += magnolia.time
        b = len(a)
        result = total_time / b
        return "Lifecycle of the buket is " + str(result)

    @staticmethod
    def sorting_by_cost():
        b = []
        for z in a:
            if z == tulip.name:
                b.append(tulip.cost)
            if z == orchid.name:
                b.append(orchid.cost)
            if z == magnolia.name:
                b.append(magnolia.cost)
        flowers_dict = dict(zip(a, b))
        sorting = sorted(flowers_dict.items(), key=lambda x: x[1])
        return sorting

    @staticmethod
    def including_flowers():
        if tulip.name in a:
            print("Tulip is in buket")
        else:
            print("Tulip is not in buket")
        if orchid.name in a:
            print("Orchid is in buket")
        else:
            print("Orchid is not in buket")
        if magnolia.name in a:
            print("Magnolia is in buket")
        else:
            print("Magnolia is not in buket")


tulip = Tulip
orchid = Orchid
magnolia = Magnolia

my_buket = Buket
