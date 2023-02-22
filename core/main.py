from homework3 import *
from homework4 import *

# hm3
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

# hm4_boolen
print(operator_i(5, 8))

print(operator_ili(5, 8))

print(slova_boolen(5, 2))

# hm4_change
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

# hm4_condition
print(positivnoe_chislo(3))

print(positive(4, 6, 8))

print(what_year(1900))

print(day_of_week(7))

print(ves(100, 1))

# hm4_dict
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

# hm4_for
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

# hm4_list
lst1 = [1, 2, 3]
lst2 = ["cat", "dog", "parrot"]
print(listss(lst1, lst2))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(common(a, b))

lst = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
print(unic(lst))

# hm4_string
str = "KatyaSank"
print(symbols(str))

str1 = "HelloWorld!!"
print(srez(str1))

str3 = "my name is name"
my_name = "Katya"
print(imya(my_name, str3))

test_tring = "Hello world!"
print(letters(test_tring))

# hm4_variable
print(variab())

# hm4_while
print(proiz(4))

print(flowers(2, 5))

print(num(45))

print(family(40, 5))
