# Домашнее задание
# Привести к целому типу -1.6, 2.99


def convert_to_celoe(x):
    return int(x)


# #Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'


def zamena(y):
    return y.replace("#", "/")


# #Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’


def dobavlenie(z):
    return z + "ing"


# #В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"


def mesta(s):
    new = s.rsplit(" ")
    return new[1] + " " + new[0]


# #Напишите программу которая удаляет пробел в начале, в конце строки


def probel(x):
    return x.lstrip().rstrip()


# #Создайте словарь, связав его с переменной school, и наполните его данными
# #которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).


def print_dict():
    a = ["1a", "2b", "3f", "4t", "5v", "6j", "7k", "8c", "9n", "10s"]
    b = [20, 19, 25, 21, 22, 22, 18, 21, 23, 25]
    school = dict(zip(a, b))
    return school


# #Создайте список и извлеките из него списка второй элемент.


def elem(l):
    return l.pop(1)


# #Вывести входит ли строка1 в строку2 (пример: employ и employment )


def vhod(x, y):
    return x in y


# #Вывести нужные символы
# # x = "My name is Agent Smith"
# # print(x[?]) #y
# # print(x[?:?:?]) #nesgt


def vihod(m):
    return m[1], m[3:16:3]
