# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
def get_reverse_num(num, reverse):
    if num != 0:
        digit = str(num % 10)
        reverse += digit
        return get_reverse_num(num // 10, reverse)
    return reverse


if __name__ == "__main__":
    reverse_num = ""
    number = input("Введите число: ")
    print("Обратное число:", get_reverse_num(int(number), reverse_num)) if number.isdigit() \
        else print("Нужно ввести число")
