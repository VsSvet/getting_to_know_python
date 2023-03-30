# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше
# заданного минимума и не больше заданного максимума).
def check_input(n: str):
    user_input = input(n)
    if user_input.isdigit():
        return int(user_input)
    return check_input(n)


numbers = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number, max_number = check_input("Минимальное число: "), check_input("Максимальное число: ")
numbers_of_given_range = [item for item in range(len(numbers)) if min_number <= numbers[item] <= max_number]
print(numbers_of_given_range)
