# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел (каждый элемент ряда
# меньше или равен предыдущему).У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют
# элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

def check_input(arg1: str):
    return arg1.isdigit()


def convert_input(arg1: str):
    return int(arg1)


def get_the_rating_index(my_list: list, arg1: int):
    index_num = len(my_list)
    for i in range(len(my_list)):
        if my_list[i] <= arg1:
            index_num = i
            break
    return index_num


def add_rating_to_list(my_list: list, index_n: int, arg: int):
    my_list.insert(index_n, arg)
    return my_list


if __name__ == "__main__":
    user_input, rating = input("Введите число: "), [7, 5, 3, 3, 2]
    user_input = convert_input(user_input) if check_input(user_input) else print("Нужно ввести число, а не строку")
    index_rating = get_the_rating_index(rating, user_input)
    rating = add_rating_to_list(rating, index_rating, user_input)
    print(f"Пользователь ввел число {user_input}. Результат: {rating}")
