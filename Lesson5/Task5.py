# Вывести на экран коды и символы таблицы ASCII, начиная с символа номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
def get_the_code_symbol(n):
    if n < 128:
        if n % 10 == 1:
            print()
        else:
            print(f"{n} - {chr(n)}", end=' ')
        return get_the_code_symbol(n + 1)


get_the_code_symbol(32)
