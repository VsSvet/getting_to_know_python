# Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся
# пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для
# вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь
# вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак
# операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
def checking_the_correct_sign(user_input):
    while user_input not in ['0', '+', '-', '*', '/']:
        user_input = input("Выберите операцию, сложение '+' , вычитание '-', умножение '*' или деление '/' или "
                           "завершить программу = 0: ")
    return user_input


def checking_division_zero(num_2, sign):
    return num_2 == "0" and sign == "/"


def get_the_result_calculation(sign, num_1, num_2):
    if sign == "+":
        return num_1 + num_2
    elif sign == "-":
        return num_1 - num_2
    elif sign == "*":
        return num_1 * num_2
    elif sign == "/":
        return num_1 / num_2


if __name__ == "__main__":
    operation_sign = checking_the_correct_sign(
        input("Выберите операцию, сложение '+' , вычитание '-', умножение '*' или деление '/' или "
              "завершить программу = 0: "))
    while operation_sign != "0":
        number_1, number_2 = input("Введите первое число: "), input("Введите второе число: ")
        if number_1.isdigit() and number_2.isdigit():
            if checking_division_zero(number_2, operation_sign):
                print("На ноль делить нельзя!")
            else:
                result = get_the_result_calculation(operation_sign, int(number_1), int(number_2))
                print(result)
        else:
            print("Нужно вводить цифры!")
        operation_sign = checking_the_correct_sign(input("Выберите операцию, сложение '+' , вычитание '-', "
                                                         "умножение '*' или деление '/' или завершить программу = 0: "))
    print("Программа завершена т.к. был введен 0")
