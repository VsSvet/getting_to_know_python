# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
def check_input(arg1: str):
    return arg1.isdigit()


def convert_input(arg1: str):
    return int(arg1)


def get_number_duplicates(arg1: list, arg2: str):
    count = arg1.count(arg2)
    return count


if __name__ == "__main__":
    count_el = input("Введите количество чисел в массиве: ")
    if check_input(count_el):
        count_el = convert_input(count_el)
        my_list = [input("Введите элемент массива: ") for el in range(count_el)]
        number = input("Введите число которое необходимо найти в списке: ")
        if not check_input(number):
            print("Введите число")
        else:
            count_duplicates = get_number_duplicates(my_list, number)
            print(f"Число {number} встречается в массиве {count_duplicates} раз")
    else:
        print("Нужно ввести число.")
