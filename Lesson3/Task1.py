# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).

def check_input(arg1: str):
    return arg1.isdigit()


def check_compliance_with_month(arg: str):
    return 0 < int(arg) < 13


def convert_input(arg1: str):
    return int(arg1)


# # Решение 1
# if __name__ == "__main__":
#     user_input = input("Введите месяц: ")
#     if check_input(user_input):
#         month = convert_input(user_input) if check_compliance_with_month(user_input) else print("Такого месяца нет.")
#         seasons = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето',
#         'Осень','Осень', 'Осень', 'Зима']
#         print(f"Время года: {seasons[month-1]}")
#     else:
#         print("Нужно ввести число.")


# Решение 2
if __name__ == "__main__":
    user_input = input("Введите месяц: ")
    if check_input(user_input):
        month = convert_input(user_input) if check_compliance_with_month(user_input) else print("Такого месяца нет.")
        seasons = {'Зима': (12, 1, 2), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
        [print(f"Время года: {k}") for k, v in seasons.items() if month in v]
    else:
        print("Нужно ввести число.")
