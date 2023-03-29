# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
def get_reverse_num(num, reverse):
    if num != 0:
        digit = str(num % 10)
        reverse += digit
        return get_reverse_num(num // 10, reverse)
    return reverse


if __name__ == "__main__":
    reverse_num = ""
    number = int(input("Введите число: "))
    reverse_num = get_reverse_num(number, reverse_num)
    print("Обратное число:", reverse_num)
