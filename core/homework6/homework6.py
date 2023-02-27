# 1 Дан файл целых чисел, содержащий не менее четырех элементов. Вывести первый, второй, предпоследний и
# последний элементы данного файла. Если чисел меньше 3 выводить ошибку


def return_element() -> tuple:
    """Return first, second, second-to-last and last elements from the file"""
    with open("ex1.txt", "r") as file:
        text: str = file.read()
        a: list = text.split()
        b: int = len(a)
        try:
            if b < 3:
                raise Exception
        except Exception:
            print("Error: В файле меньше 3 элементов")
        return a[0], a[1], a[-2], a[-1]


# 2 Дан файл целых чисел. Создать два новых файла, первый из которых содержит четные числа из исходного файла,
# а второй — нечетные (в том же порядке). Если четные или нечетные числа в исходном файле отсутствуют, то
# соответствующий результирующий файл оставить пустым.


def even_odd() -> None:
    """Create two files with odd/even numbers from file"""
    with open("ex2.txt", "r") as common_file, open("ex2_1.txt", "w") as f1, open(
        "ex2_2.txt", "w"
    ) as f2:
        res1: list = []
        res2: list = []
        text1 = common_file.read()
        a: list = text1.split(",")
        nums: list = [int(s) for s in a]
        for y in nums:
            if y % 2 == 0:
                res1.append(y)
            else:
                res2.append(y)
        if res1 != []:
            f1.writelines(str(res1))
        if res2 != []:
            f2.writelines(str(res2))
        return


# 3 Дан файл вещественных чисел. Заменить в нем все элементы на их квадраты.


def num_in_pow() -> None:
    """Overwrite numbers to square into the file"""
    with open("ex3.txt", "rt+") as file3:
        s: list = []
        result: list = []
        v: str = file3.read()
        w: list = v.split(",")
        s: list = [int(b) for b in w]
        for j in s:
            j: int = j**2
            result.append(j)
    with open("ex3.txt", "wt+") as file3:
        file3.write(str(result))
        return


# 4 Даны два файла произвольного типа. Поменять местами их содержимое. Файлы должны быть бинарного типа


def swap_content() -> None:
    """Swap data into 2 files"""
    with open("1.bin", "rb+") as fileb1, open("2.bin", "rb") as fileb2:
        a: bytes = fileb1.read()
        b: bytes = fileb2.read()
    with open("1.bin", "wb+") as fileb1, open("2.bin", "wb+") as fileb2:
        fileb1.write(b)
        fileb2.write(a)
        return
