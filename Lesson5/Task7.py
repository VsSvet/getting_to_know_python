# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется
# равенство:1+2+...+n = n(n+1)/2, где n - любое натуральное число.
from sys import setrecursionlimit
setrecursionlimit(2300)


def get_user_input():
    user_input = input("Введите натуральное число от 1 до 2000: ")
    if user_input.isdigit() and (0 < int(user_input) < 2001):
        return int(user_input)
    return get_user_input()


def sum_numbers(num):
    if num > 0:
        return num + sum_numbers(num - 1)
    return num


if __name__ == "__main__":
    number = get_user_input()
    checking_expression, result = number * (number + 1) / 2, sum_numbers(number)
    if result == checking_expression:
        print(f"Для числа {number} верно равенство 1+2+...+n = n(n+1)/2")
