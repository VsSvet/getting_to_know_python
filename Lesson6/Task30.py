# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести
# с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.
def check_input(n:str):
    user_input = input(n)
    if user_input.isdigit():
        return int(user_input)
    return check_input(n)


number1, difference, count_el = check_input("Элемент №1: "), check_input("Разность: "), check_input("Количество: ")
arithmetic_progression = [(number1 + (item - 1) * difference) for item in range(1, count_el + 1)]
print(*arithmetic_progression)
