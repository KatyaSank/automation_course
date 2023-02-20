# 1. Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов.
# Извлеките из строки первый символ, затем последний, третий с начала и третий с
# конца. Измерьте длину вашей строки.

str = "KatyaSank"
print(str[0])
print(str[-1])
print(str[2])
print(str[-3])
print(len(str))

# 2. Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из
# нее следующие срезы:
# ● первые восемь символов
# ● четыре символа из центра строки
# ● символы с индексами кратными трем
# ● переверните строку

str1 = "HelloWorld!!"
print(str1[0:8])
print(str1[4:8])
print(str1[3:12:3])
reversed = "".join(reversed(str1))
print(reversed)

# 3. Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте
# ваше имя.

str3 = "my name is name"
print(str3[:11] + "Katya")

# 4. Есть строка: test_tring = "Hello world!", необходимо
# ● напечатать на каком месте находится буква w
# ● кол-во букв l
# ● Проверить начинается ли строка с подстроки: “Hello”
# ● Проверить заканчивается ли строка подстрокой: “qwe”

test_tring = "Hello world!"
print(test_tring.find("w"))
print(test_tring.count("l"))
print(test_tring.startswith("Hello"))
print(test_tring.endswith("qwe"))
