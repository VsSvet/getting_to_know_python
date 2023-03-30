# Подсчитать четные и нечетные цифры введенного натурального числа.
def check_the_even_or_odd_number(num, even_number, odd_number):
    remainder_of_number = num % 10
    if remainder_of_number % 2 == 0:
        even_number += 1
    else:
        odd_number += 1
    return even_number, odd_number


def get_number_even_and_odd_numbers(num, count_even, count_odd, check_even_or_odd_number):
    if num == 0:
        print(f"В числе {number} четных - {count_even}, нечетных - {count_odd}")
    else:
        count_even, count_odd = check_the_even_or_odd_number(num, count_even, count_odd)
        num = num // 10
        get_number_even_and_odd_numbers(num, count_even, count_odd, check_even_or_odd_number)


if __name__ == "__main__":
    count_of_even, count_of_odd = 0, 0
    number = input("Введите число: ")
    get_number_even_and_odd_numbers(int(number), count_of_even, count_of_odd, check_the_even_or_odd_number) \
        if number.isdigit() else print("Нужно ввести число")
