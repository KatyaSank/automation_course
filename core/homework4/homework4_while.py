import unittest


# 1. Дано число N. Найти произведение всех чисел от 0 до N.

def proiz(N):
    itogo = 1
    x = 0
    if N == 0:
        return "Incorrect number"
    if N < 0:
        return "Incorrect number : negative"
    if type(N) is not int:
        return "Incorrect number : type error"
    if N is False:
        return "Incorrect number"
    while x < N:
        x += 1
        itogo *= x
    return itogo


class TestProiz(unittest.TestCase):
    def test_poz(self):
        self.assertEqual(proiz(2), 2, "Error in test_poz")

    def test_max(self):
        self.assertEqual(proiz(50), 30414093201713378043612608166064768844377641568960512000000000000,
                         "Error in test_max")

    def test_0(self):
        self.assertEqual(proiz(0), "Incorrect number", "Error in test_0")

    def test_negative(self):
        self.assertEqual(proiz(-2), "Incorrect number : negative", "Error in test_negative")

    def test_1(self):
        self.assertEqual(proiz(1), 1, "Error in test_1")

    def test_float(self):
        self.assertEqual(proiz(3.5), "Incorrect number : type error", "Error in test_float")

    def test_false(self):
        self.assertEqual(proiz(False), "Incorrect number", "Error in test_false")

    def test_true(self):
        self.assertEqual(proiz(True), "Incorrect number : type error", "Error in test_true")


# Чек-лист
# N > 0
# N = 0
# N = -1
# N = 1
# N > 100000000000000
# N цифры+буквы
# N цифры+символы
# N цифры+пробелы
# Дробное с одним числом после запятой
# Дробное с пятью числами после запятой
# Спецсимволы, буквы
# Пробелы, NULL
# Инджекшн


# 2. Поле засеяли цветами двух сортов на площади S1 и S2. Каждый год
# площадь цветов первого сорта увеличивается вдвое, а площадь второго сорта
# увеличивается втрое. Через сколько лет площадь первых сортов будет
# составлять меньше 10% от площади вторых сортов.


def flowers(S1, S2):
    x = 0
    if S1 < 0 or S2 < 0:
        return "Incorrect number"
    if S1 == 0 or S2 == 0:
        return "Incorrect number"
    if type(S1) is not int or type(S2) is not int:
        return "Incorrect number : type error"
    while S1 > 0.1 * S2:
        S1 *= 2
        S2 *= 3
        x += 1
    return x


class TestFlowers(unittest.TestCase):
    def test_poz(self):
        self.assertEqual(flowers(2, 2), 6, "Error in test_poz")

    def test_max(self):
        self.assertEqual(flowers(200, 32), 11, "Error in test_max")

    def test_neg(self):
        self.assertEqual(flowers(-2, -5), "Incorrect number", "Error in test_neg")

    def test_one_neg(self):
        self.assertEqual(flowers(2, -2), "Incorrect number", "Error in test_one_neg")

    def test_float(self):
        self.assertEqual(flowers(2.5, 2.1), "Incorrect number : type error", "Error in test_float")

    def test_0(self):
        self.assertEqual(flowers(0, 0), "Incorrect number", "Error in test_0")

    def test_one_0(self):
        self.assertEqual(flowers(0, 5), "Incorrect number", "Error in test_one_0")

    def test_one_float(self):
        self.assertEqual(flowers(2, 2.5), "Incorrect number : type error", "Error in test_one_float")


# Чек-лист
# S1, S2 положительные (целые)
# S1, S2 отрицательные (целые)
# S1 положительное, S2 отрицательное (целые)
# S1 отрицательное, S2 положительное (целые)
# S1, S2 дроби с 1 знаком после запятой
# S1, S2 дроби с 9 знаками после запятой
# S1, S2 целые с 1 знаком
# S1, S2 целые с 10 знаками
# S1 целые, S2  дробь
# S1, S2 числа + буквы (6g)
# S1, S2 числа + пробелы (7 )
# S1, S2 числа + символы (3*)
# S1, S2 0
# Одно из чисел 0
# Спецсимволы, буквы
# Пробелы, NULL
# Инджекшн


# 3. Дано целое число N (>0). Используя операции деления нацело и взятия
# остатка от деления, найти количество и сумму его цифр.


def num(N):
    a = 0
    b = 0
    while N > 0:
        N //= 10
        a += 1
        b += N % 10
    return a, b


# 4. Деду M лет, а внуку N лет. Через сколько лет дед станет вдвое старше
# внука. И сколько при этом лет будет деду и внуку.


def family(M, N):
    x = 0
    while M > N * 2:
        x += 1
        M += 1
        N += 1
    return x, M, N
