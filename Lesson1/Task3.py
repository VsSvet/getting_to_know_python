# Задание 3.
# Узнайте у пользователя целое положительное число n. Найдите сумму чисел n + nn + nnn.

number = input("Введите число n: ")
print(f"Сумма чисел n + nn + nnn = {int(number) + int(number * 2) + int(number * 3)}")
