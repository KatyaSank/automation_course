# Преобразование типов
# 1. Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]


def stroka_v_mas(a, b):
    new_a = a.split()
    new_b = b.split()
    return new_a, new_b


# 2. Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”


def formatir_strok(lst1, str1, str2):
    str3 = " ".join(lst1)
    str3_1 = str3.replace(",", "")
    return f"Привет,{str3}! Добро пожаловать в {str1} {str2}"


# 3. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него
# строку => "I love arrays they are my favorite"


def spisok_v_stroki(lst):
    str = " ".join(lst)
    str1 = str.replace(",", "")
    return str1


# 4. Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6


def redaktir_spisok(spis):
    spis.insert(2, "cat")
    spis.pop(6)
    return spis


# 5.
# Есть 2 словаря
# a = { 'a': 1, 'b': 2, 'c': 3}
# b = { 'c': 3, 'd': 4,'e': 5}
# Необходимо их объединить по ключам, а значения ключей поместить в список, если у
# одного словаря есть ключ "а", а у другого нету, то поставить значение None на
# соответствующую позицию(1-я позиция для 1-ого словаря, вторая для 2-ого)
# ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}

a = {"a": 1, "b": 2, "c": 3}
b = {"c": 3, "d": 4, "e": 5}

# *1) Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число
# *2) Дан текст, который содержит различные английские буквы и знаки препинания. Вам
# необходимо найти самую частую букву в тексте. Результатом должна быть буква в
# нижнем регистре.
# При поиске самой частой буквы, регистр не имеет значения, так что при подсчете
# считайте, что "A" == "a". Убедитесь, что вы не считайте знаки препинания, цифры и
# пробелы, а только буквы.
# Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет
# буква, которая идет первой в алфавите. Для примера, "one" содержит "o", "n", "e" по
# одному разу, так что мы выбираем "e".
# "a-z" == "a"
# "Hello World!" == "l"
# "How do you do?" == "o"
# "One" == "e"
# "Oops!" == "o"
# "AAaooo!!!!" == "a"
# "a" * 9000 + "b" * 1000 == "a"
