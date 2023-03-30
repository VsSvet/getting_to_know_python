# Напишите программу, на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
def exponentiation(a, b):
    if b > 0:
        return a * exponentiation(a, b - 1)
    return 1


basis, indicator = input("Введите основание степени: "), input("Введите показатель степени: ")
if basis.isdigit() and indicator.isdigit():
    basis, indicator = int(basis), int(indicator)
    result = exponentiation(basis, indicator)
    print(f"Число {basis} в степени {indicator} равно {result}")
else:
    print("Нужно ввести число, а не строку")
