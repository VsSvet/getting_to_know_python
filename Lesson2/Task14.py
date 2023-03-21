# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
try:
    n = int(input("Введите число: "))
    print(*[2 ** item for item in range(n) if 2 ** item < n])
except ValueError:
    print("Вы ввели строку!")
