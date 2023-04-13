from random import randint
import unittest


# 1. Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B
# включительно.


def celye_chisla(A, B):
    try:
        n = 0
        for x in range(A, B + 1):
            n += x
        return n
    except TypeError:
        return "Incorrect type"


class TestCelye(unittest.TestCase):
    def test_poz(self):
        self.assertEqual(celye_chisla(2, 5), 14, "Error in test_poz")

    def test_max(self):
        self.assertEqual(celye_chisla(2, 50000), 1250024999, "Error in test_max")

    def test_neg(self):
        self.assertEqual(celye_chisla(-5, -2), -14, "Error in test_neg")

    def test_neg_and_pos(self):
        self.assertEqual(celye_chisla(-2, 2), 0, "Error in test_neg_and_pos")

    def test_float(self):
        self.assertEqual(celye_chisla(0.2, 5.3), "Incorrect type", "Error in test_float")

    def test_float_and_int(self):
        self.assertEqual(celye_chisla(1.3, 5), "Incorrect type", "Error in test_float_and_int")

    def test_int_and_float(self):
        self.assertEqual(celye_chisla(3, 10.2), "Incorrect type", "Error in test_int_and_float")

    def test(self):
        self.assertEqual(celye_chisla(5, 2), 0, "Error in test")

    def test_0(self):
        self.assertEqual(celye_chisla(0, 0), 0, "Error in test_0")

    def test_one_string(self):
        self.assertEqual(celye_chisla(2, '4k'), "Incorrect type", "Error in test_one_string")


# Чек-лист
# А<В целые, позитивные числа с 1 знаком
# А<В целые, позитивные числа с 10 знаками
# А<В целые, негативные числа с 1 знаком
# А<В целые, негативные числа с 10 знаками
# А<В негативные + позитивные числа
# А<В дробное
# A дробное, B целое
# A целое, B дробное
# А>В целое
# А=В целое
# Оба 0
# A(0)<B
# A<B(0)
# А - цифры, B - буквы
# A, B цифры+буквы (6а)
# A, B цифры+символы (6?)
# A, B цифры+пробелы (6 )
# Спецсимволы, буквы
# Пробелы, NULL
# Инджекшн


# 2. Найти сумму всех натуральных чисел в от A до B


def natur_chisla(A, B):
    n = 0
    for x in range(A + 1, B):
        if x > 0:
            n += x
    return n


# 3. Найти произведение положительных, сумму и количество отрицательных
# из 10 введенных целых значений.


def proizvedenie(numbers):
    m1 = 1
    m2 = 0
    m3 = 0
    for n in numbers:
        if n > 0:
            m1 *= n
        elif n < 0:
            m2 += n
            m3 += 1
        return m1, m2, m3


# 4. Дан словарь пловцов с их результатами. Напечатать лучший результат
# заплыва среди 6 участников.
# Бекиш Александр - 21,07
# Будник Алексей - 20,34
# Гребень Анастасия - 22,12
# Давидович Татьяна - 30
# Дешук Дмитрий - 24.01
# Казак Анна - 28,17


def winner(**slv):
    return min(slv.values())


# 5. Есть массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5. Напишите программу, которая будет выводить
# уникальное число


def unical(mas):
    for i in mas:
        a = mas.count(i)
        if a == 1:
            return i
