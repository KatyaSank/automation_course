import time

# Написать обычную функцию для факториала, генератор и рекурсию. Сравнить их время работы
# Обычная функция
start = time.time()


def usual_fun(n):
    m = 1
    for i in range(1, n + 1):
        m *= i
    return m


finish = time.time()
print("Result time = " + str(finish - start))

# генератор
start = time.time()


def gen(t):
    m1 = 1
    for i in range(1, t + 1):
        m1 *= i
        yield m1


finish = time.time()
print("Result time = " + str(finish - start))

# Рекурсия
start = time.time()


def recur(a):
    while a > 1:
        return a * recur(a - 1)
    else:
        return a


finish = time.time()
print("Result time = " + str(finish - start))


# Напишите декоратор, который проверял бы тип параметров функции, конвертировал их если надо и складывал:
# 1
def typed(fun):
    def wrapper(arg1, arg2):
        arg1 = str(arg1)
        arg2 = str(arg2)
        return fun(arg1, arg2)

    return wrapper


@typed
def add_two_symbols(a, b):
    return a + b


# 2
def typed2(func):
    def wrapper(arg1, arg2, arg3):
        if type(arg1) == str:
            arg1 = int(arg1)
        return func(arg1, arg2, arg3)

    return wrapper


@typed2
def add_three_symbols(a, b, c):
    return a + b + c


# На вход подаётся некоторое количество (не больше сотни) разделённых пробелом целых чисел (каждое не меньше 0 и не
# больше 19). Выведите их через пробел в порядке лексикографического возрастания названий этих чисел в
# английском языке.Т.е., скажем числа 1, 2, 3 должны быть выведены в порядке 1, 3, 2, поскольку слово two в словаре
# встречается позже слова three, а слово three -- позже слова one (иначе говоря, поскольку выражение
# 'one' < 'three' < 'two' является истинным)

b = []
result = []


def len_of_num(number_names):
    for k, v in number_names.items():
        a = (k, len(v))
        b.append(a)
        b.sort(key=lambda x: x[1])

    for x in b:
        result.append(x[0])
    return result
