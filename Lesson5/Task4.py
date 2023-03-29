# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ... Количество элементов (n) вводится с клавиатуры.
def get_sum_elements(count_num, el_row, sum_el):
    if count_num > 0:
        return get_sum_elements(count_num-1, el_row / -2, sum_el + el_row)
    return sum_el


if __name__ == "__main__":
    el_1 = 1
    sum_elements = 0
    count_number = input("Введите количество элементов ряда: ")
    print(f"Сумма элементов равна {get_sum_elements(int(count_number), el_1, sum_elements)}") if count_number.isdigit()\
        else print("Нужно ввести число")
