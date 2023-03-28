# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических
# операций допускаются только +1 и -1. Также нельзя использовать циклы.
def sum_numbers(int1, int2):
    if int2 > 0:
        return sum_numbers(int1 + 1, int2 - 1)
    return int1


number_1, number_2 = input("Введите первое слагаемое: "), input("Введите второе слагаемое: ")
if number_1.isdigit() and number_2.isdigit():
    number_1, number_2 = int(number_1), int(number_2)
    result = sum_numbers(number_1, number_2)
    print(f"Сумма чисел равна {result}")
else:
    print("Нужно ввести число, а не строку")
