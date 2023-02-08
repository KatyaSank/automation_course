# Домашнее задание

flt1 = 1.6
flt2 = 2.99
int_1 = int(flt1)
int_2 = int(flt2)
print(int_1)
print(int_2)

str = 'www.my_site.com#about'
print(str.replace('#', '/'))

word = 'stroka'
print(word + 'ing')

stroka = 'Ivanou Ivan'
new = stroka.rsplit(' ')
print(new[1] + ' ' + new[0])

animal = ' cat '
print(animal.lstrip().rstrip())

school = {'1a': 20, '2b': 19, '3f': 25, '4t': 21, '5v': 22, '6j': 22, '7k': 18, '8c': 21, '9n': 23, '10s': 25}
print(type(school))

lst = [1, 2, 3, 9]
print(lst.pop(1))

str1 = 'employ'
str2 = 'employment'
print(str1 in str2)

x = "My name is Agent Smith"
print(x[1])  # y
print(x[3:16:3])  # nesgt
