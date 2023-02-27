from homework3 import *
from homework4 import *
from homework8 import *

print(
    "hm3____________________________________________________________________________________________________________"
)
print(convert_to_celoe(1.6))
print(convert_to_celoe(2.99))

print(zamena("www.my_site.com#about"))

print(dobavlenie("stroka"))

print(mesta("Ivanou Ivan"))

print(probel(" cat "))

print(print_dict())

print(elem([1, 2, 3, 9]))

print(vhod("employ", "employment"))

print(vihod("My name is Agent Smith"))

print(
    "hm4_boolen_____________________________________________________________________________________________________"
)
print(operator_i(5, 8))

print(operator_ili(5, 8))

print(slova_boolen(5, 2))

print(
    "hm4_change_____________________________________________________________________________________________________"
)
a = "Robin Singh"
b = "I love arrays they are my favorite"
print(stroka_v_mas(a, b))

lst1 = ["Ivan", "Ivanou"]
str1 = "Minsk"
str2 = "Belarus"
print(formatir_strok(lst1, str1, str2))

lst = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(spisok_v_stroki(lst))

spis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(redaktir_spisok(spis))

print(
    "hm4_condition__________________________________________________________________________________________________"
)
print(positivnoe_chislo(3))

print(positive(4, 6, 8))

print(what_year(1900))

print(day_of_week(7))

print(ves(100, 1))

print(
    "hm4_dict_______________________________________________________________________________________________________"
)
school = {
    "1a": 20,
    "2b": 19,
    "3f": 25,
    "4t": 21,
    "5v": 22,
    "6j": 22,
    "7k": 18,
    "8c": 21,
    "9n": 23,
    "10s": 25,
}
print(sch(school))

print(
    "hm4_for________________________________________________________________________________________________________"
)
print(celye_chisla(0, 8))

print(natur_chisla(1, 10))

numbers = [randint(-100, 100) for _ in range(10)]
print(proizvedenie(numbers))

slv = {
    "Бекиш Александр": 21.07,
    "Будник Алексей": 20.34,
    "Гребень Анастасия": 22.12,
    "Давидович Татьяна": 30,
    "Дешук Дмитрий": 24.01,
    "Казак Анна": 28.17,
}
print(winner(**slv))

mas = [1, 5, 2, 9, 2, 9, 1]
print(unical(mas))

print(
    "hm4_list_______________________________________________________________________________________________________"
)
lst1 = [1, 2, 3]
lst2 = ["cat", "dog", "parrot"]
print(listss(lst1, lst2))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(common(a, b))

lst = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
print(unic(lst))

print(
    "hm4_string_____________________________________________________________________________________________________"
)
str = "KatyaSank"
print(symbols(str))

str1 = "HelloWorld!!"
print(srez(str1))

str3 = "my name is name"
my_name = "Katya"
print(imya(my_name, str3))

test_tring = "Hello world!"
print(letters(test_tring))

print(
    "hm4_variable___________________________________________________________________________________________________"
)
print(variab())

print(
    "hm4_while______________________________________________________________________________________________________"
)
print(proiz(4))

print(flowers(2, 5))

print(num(45))

print(family(40, 5))

print(
    "hm8____________________________________________________________________________________________________________"
)
print(usual_fun(7))

for m1 in gen(7):
    print(m1)

print(recur(7))

print(add_two_symbols("3", 5))  # -> "35"
print(add_two_symbols(5, 5))  # -> "55"
print(add_two_symbols("a", "b"))  # -> 'ab’

print(add_three_symbols(5, 6, 7))  # -> 18
print(add_three_symbols("3", 5, 0))  # -> 8
print(add_three_symbols(0.1, 0.2, 0.4))  # -> 0.7000000000000001

number_names = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

print(len_of_num(number_names))
