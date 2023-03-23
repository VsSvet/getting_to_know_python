# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
def check_input(arg1: str):
    return arg1.isdigit()


def convert_input(arg1: str):
    return int(arg1)


def get_index_number(my_list_num: list, num: str):
    num, index = convert_input(num), 0
    min_diff = abs(num - my_list_num[0])
    for k in range(1, len(my_list_num)):
        diff_el = abs(num - my_list[k])
        if diff_el < min_diff:
            min_diff, index = diff_el, k
    return index


if __name__ == "__main__":
    count_el = input("Введите количество чисел в массиве: ")
    count_el = convert_input(count_el) if check_input(count_el) else print("Нужно ввести число.")
    my_list = []
    for i in range(count_el):
        user_input = input("Введите элемент массива: ")
        my_list.append(convert_input(user_input)) if check_input(user_input) else print("Нужно вводить числа")
    number = input("Введите число которое необходимо найти в списке: ")
    index_number = get_index_number(my_list, number) if check_input(number) else print("Введите число")
    print(f"В массиве число {my_list[index_number]} самый близкий по величине элемент к числу {number}")
