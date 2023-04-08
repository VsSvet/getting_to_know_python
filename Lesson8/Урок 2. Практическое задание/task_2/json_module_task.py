from json import dump, load


def write_order_to_json(item: str, quantity: int, price: int, buyer: str, date: str):
    with open('orders.json') as f_n:
        j_ob = load(f_n)
    j_ob['orders'].append({'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date})
    with open('orders.json', 'w') as f_n:
        dump(j_ob, f_n, indent=4, separators=(', ', ': '))


if __name__ == '__main__':
    write_order_to_json("computer", 1, 70000, "Vostrov M.S.", "11.01.2018")
