# Условия
# 1. Дано целое число. Если оно является положительным, то прибавить к нему 1; в
# противном случае не изменять его. Вывести полученное число.

per = 10
if per > 0:
    per += 1
    print(per)
else:
    print(per)

# 2. Даны три целых числа. Найти количество положительных чисел в исходном
# наборе.

a = 4
b = 6
c = 3
n = 0

lst = [a, b, c]
for x in lst:
    if x > 0:
        n += 1
print(n)

# 3. Дан номер года (положительное целое число). Определить количество дней в
# этом году, учитывая, что обычный год насчитывает 365 дней, а високосный — 366
# дней. Високосным считается год, делящийся на 4, за исключением тех годов, которые
# делятся на 100 и не делятся на 400 (например, годы 300, 1300 и 1900 не являются
# високосными, а 1200 и 2000 являются).

year = 1900

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 != 0:
            print("365 дней в году")
        else:
            print("366 дней в году")

# 4. Дано целое число в диапазоне 1–7. Вывести строку — название дня недели,
# соответствующее данному числу (1 — «понедельник», 2 — «вторник» и т. д.).

x = 4

if x == 1:
    print("понедельник")
elif x == 2:
    print("вторник")
elif x == 3:
    print("среда")
elif x == 4:
    print("четверг")
elif x == 5:
    print("пятница")
elif x == 6:
    print("суббота")
else:
    print("воскресенье")

# 5. Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 —
# миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер. Дан номер единицы массы (целое
# число в диапазоне 1–5) и масса тела в этих единицах (вещественное число). Найти
# массу тела в килограммах.

a = 100
b = 3

if b == 1:
    print("Масса тела равна " + str(a) + " кг.")
elif b == 2:
    x = a / 1000000
    print("Масса тела равна " + str(x) + " кг.")
elif b == 3:
    x = a / 1000
    print("Масса тела равна " + str(x) + " кг.")
elif b == 4:
    x = a * 1000
    print("Масса тела равна " + str(x) + " кг.")
elif b == 5:
    x = a / 100
    print("Масса тела равна " + str(x) + " кг.")
