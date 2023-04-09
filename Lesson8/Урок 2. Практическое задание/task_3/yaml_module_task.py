from yaml import dump, safe_load


def get_yaml_file(file: str, items_dict: dict):
    with open(file, 'w') as outfile:
        dump(items_dict, outfile, default_flow_style=True, allow_unicode=True)


def check_yaml_file(file: str, items_dict: dict):
    with open(file, 'r') as file_read:
        return safe_load(file_read) == items_dict


if __name__ == '__main__':
    items = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
             'items_quantity': 4,
             'items_ptice': {'computer': '200€-1000€', 'keyboard': '5€-50€', 'mouse': '4€-7€', 'printer': '100€-300€'}}
    get_yaml_file("file.yaml", items)
    if check_yaml_file("file.yaml", items):
        print("Данные из созданного файла, совпадают с исходными.")
