# Найдите сумму цифр трехзначного числа.

number = int(input("Введите трехзначное число: "))
sum_numbers = 0

while number > 0:
    sum_numbers += number%10
    number = number // 10

print(f"Сумма чисел трехзначного числа равна {sum_numbers}")