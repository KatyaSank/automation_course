# 1. Создайте словарь, связав его с переменной school, и наполните его данными,
# которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б,
# 2б, 6а, 7в и т.д.).
# 2. Узнайте сколько человек в каком-нибудь классе.
# 3. Представьте, что в школе произошли изменения, внесите их в словарь:
# ◦ в трех классах изменилось количество учащихся;
# ◦ в школе появилось два новых класса;
# ◦ в школе расформировали один из классов.
# 4. Выведите содержимое словаря на экран.

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
print(school.get("6j"))
upd = {"5v": 40, "8c": 45, "10s": 50}
upd1 = {"11y": 17, "12l": 19}

school.update(upd)
print(school)

school.update(upd1)
print(school)

school.pop("1a")
print(school)
