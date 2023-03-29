# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
# попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что
# загадано. Если за 10  попыток число не отгадано, то вывести загаданное число. Решите через рекурсию. В задании
# нельзя применять циклы.
from random import randint


def checking_the_correct_user_input(user_input):
    if user_input.isdigit() and (0 <= int(user_input) < 101):
        return int(user_input)
    return checking_the_correct_user_input(input("Введите число от 0 до 100: "))


def guess_number(checking_the_correct_input, ridd, attempt):
    user_input = checking_the_correct_input(input("Введите число от 0 до 100: "))
    if attempt > 0:
        print(f"Осталось {attempt} попыток.")
        if user_input == ridd:
            print(f"Верно! Было загадано число {ridd}")
        elif user_input < ridd:
            print("Число меньше загаданного:")
            return guess_number(checking_the_correct_input, ridd, attempt - 1)
        else:
            print("Число больше загаданного:")
            return guess_number(checking_the_correct_input, ridd, attempt - 1)
    else:
        print(f"Жаль, но попытки закончились. Ты програл. Было загадано число {ridd}")


if __name__ == "__main__":
    print("Привет! Попробуй отгадать число, что я загадал! У тебя будет 10 попыток! Подсказка это число от 0 до 100.")
    riddle, attempts = randint(0, 101), 9
    guess_number(checking_the_correct_user_input, riddle, attempts)
