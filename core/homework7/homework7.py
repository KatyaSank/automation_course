# 1 Создать lambda функцию, которая принимает на вход имя и выводит его в формате “Hello, {name}”

fun = lambda name: f"Hello, {name}"


# 2 Создать lambda функцию, которая принимает на вход список имен и выводит их в формате “Hello, {name}” в
# другой список


def list_of_names(x, operation):
    lst2 = []
    for name in x:
        result = operation(name)
        lst2.append(result)
    print(lst2)


# 3 Напишите генератор который принимает список numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7] и
# возвращает новый список только с положительными числами


pos = []
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]


def positive_num(numbers):
    for x in numbers:
        if x > 0:
            yield x


for x in positive_num(numbers):
    pos.append(x)

print(pos)

# 4 Необходимо составить список чисел которые указывают на длину слов в строке: sentence = " thequick
# brown fox jumps over the lazy dog", но только если слово не "the" с обработкой исключений

results = []
sentence = " thequick brown fox jumps over the lazy dog"


def count_length(sentence):
    s = sentence.split()
    for a in s:
        try:
            if a != "the":
                yield a
            else:
                raise Exception('Error : word "the"')
        except Exception as instance:
            print(instance)


for a in count_length(sentence):
    results.append(len(a))

print(results)
