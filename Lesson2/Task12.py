# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму
# этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
import math

# Решение 1
# try:
#     sum_numbers, product_numbers = int(input("Введите сумму чисел: ")), int(input("Введите произведение чисел: "))
#     d = sum_numbers ** 2 - 4 * product_numbers
#     number1, number2 = int((sum_numbers + math.sqrt(d)) / 2), int((sum_numbers - math.sqrt(d)) / 2)
#     print(f"Петя загадал числа: {number1} и {number2}") if number1 + number2 == sum_numbers else print(
#         "Вы ввели неправильные сумму или произведение")
# except ValueError as err:
#     print(f"Вы ввели неправильные сумму или произведение {err}")


# Решение 2
def check_input(arg1: str, arg2: str):
    return arg1.isdigit() and arg2.isdigit()


def convert_input(arg1: str, arg2: str):
    return int(arg1), int(arg2)


def get_discriminant(b: int, c: int):
    return b ** 2 - 4 * c


def get_roots(b: int, discr: int):
    if discr < 0:
        return 0
    root1, root2 = int((b + math.sqrt(discr)) / 2), int((b - math.sqrt(discr)) / 2)
    if root1 + root2 == b:
        return root1, root2
    return 0


if __name__ == "__main__":
    input1, input2 = input("Введите сумму чисел: "), input("Введите произведение чисел: ")
    if check_input(input1, input2):
        sum_numbers, product_numbers = convert_input(input1, input2)
        roots = get_roots(sum_numbers, get_discriminant(sum_numbers, product_numbers))
        if roots:
            print(f"Петя загадал числа: {roots[0]} и {roots[1]}")
        else:
            print("Вы ввели неправильные сумму или произведение")
    else:
        print("Нужно ввести число, а не строку")
