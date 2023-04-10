import unittest


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
    if x is False or x is True:
        return "Incorrect number"
    if type(x) is not str:
        return "Incorrect number : type error"
    return x.lstrip().rstrip()


class TestProbel(unittest.TestCase):
    def test_without_spaces(self):
        self.assertEqual(probel('hello'), 'hello', "Error in test_without_spaces")

    def test_with_spaces(self):
        self.assertEqual(probel(' hello '), 'hello', "Error in test_with_spaces")

    def test_with_space_start(self):
        self.assertEqual(probel(' hello'), 'hello', "Error in test_with_space_start")

    def test_with_space_end(self):
        self.assertEqual(probel('hello '), 'hello', "Error in test_with_space_end")

    def test_with_space_middle(self):
        self.assertEqual(probel('hel lo'), 'hel lo', "Error in test_with_space_end")

    def test_with_two_spaces(self):
        self.assertEqual(probel('  hello  '), 'hello', "Error in test_with_two_spaces")

    def test_one_sign(self):
        self.assertEqual(probel('m'), 'm', "Error in test_one_sign")

    def test_string_with_symbols(self):
        self.assertEqual(probel('test_with_space_end'), 'test_with_space_end', "Error in test_string_with_symbols")

    def test_empty_string(self):
        self.assertEqual(probel(''), '', "Error in test_empty_string")

    def test_string_with_space(self):
        self.assertEqual(probel(' '), '', "Error in test_string_with_space")

    def test_false(self):
        self.assertEqual(probel(False), "Incorrect number", "Error in test_false")

    def test_true(self):
        self.assertEqual(probel(True), "Incorrect number", "Error in test_false")

    def test_number(self):
        self.assertEqual(probel(5), "Incorrect number : type error", "Error in test_number")


# Чек-лист
# Строка без пробелов в начале и в конце
# Строка с пробелом в начале и в конце
# Строка только с пробелом в начале
# Строка только с пробелом в конце
# Строка с пробелом посередине
# Строка состоит из нескольких строк
# Строка из 1 пробела в начале и в конце
# Строка из 2 пробелов в начале и конце
# Строка длинною в 1 символ
# Строка длинною 100000 символов
# Пустая строка
# Пробелы, NULL
# Не строковый тип(число, множество, словарь, ссылка, картинка и т.д.)
# Инджекшн


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
