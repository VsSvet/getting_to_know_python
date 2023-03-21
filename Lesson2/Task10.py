# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

def check_input(arg1: str):
    return arg1.isdigit()


def convert_input(arg1: str):
    return int(arg1)


def get_number_of_heads_and_tails(number_coins: int):
    count_zero, count_one = 0, 0
    while number_coins > 0:
        x = input(f"Какой стороной лежит монета {number_coins}, 0 - решка, 1 - орел: ")
        if check_input(x):
            coin = convert_input(x)
            if coin == 0:
                count_zero += 1
                number_coins -= 1
            elif coin == 1:
                count_one += 1
                number_coins -= 1
            else:
                print("Нужно ввести 0 или 1")
        else:
            print("Нужно ввести число")
    return count_zero, count_one


def get_least_amount_coins(count_h: int, count_t: int):
    if count_t > count_h:
        return count_heads
    return count_tails


if __name__ == "__main__":
    user_input = input("Сколько монеток на столе: ")
    if check_input(user_input):
        number_of_coins = convert_input(user_input)
        count_heads, count_tails = get_number_of_heads_and_tails(number_of_coins)
        print(f"Перевернуть нужно {get_least_amount_coins(count_heads, count_tails)} монет")
    else:
        print("Нужно ввести число")

