# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре
def check_input(arg1: str):
    return arg1.isdigit()


def convert_input(arg1: str):
    return int(arg1)


product_keys, count_product = ['название', 'цена', 'количество', 'ед'], input("Сколько товаров будет?")
if check_input(count_product):
    count_product = convert_input(count_product)
    my_list = [(i, dict(название=input("Введите название товара: "), цена=input("Введите цену товара: "),
               количество=input("Введите количество товара: "), ед=input("Введите единицу измерения: "))) for i
               in range(1, count_product + 1)]
    print("Товары")
    [print(f"{key}: {value}") for key, value in dict(my_list).items()]
    product_values = [[my_list[i][1][k] for i in range(count_product)] for k in product_keys]
    analytics = dict(zip(product_keys, product_values))
    [print(f"{key}: {value}") for key, value in analytics.items()]
else:
    print("Нужно ввести число")
