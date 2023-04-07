from csv import DictWriter
from re import findall


def get_data(files_list):
    main_data = [[" ", "Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]]
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    for file in files_list:
        with open(file) as f_obj:
            for line in f_obj:
                if findall(r'Изготовитель системы:\s*\S*', line):
                    os_prod_list.append(findall(r'Изготовитель системы:\s*\S*', line)[0].split()[-1])
                elif findall(r'Название ОС:\s*\S*', line):
                    os_name_list.append(findall(r'Название ОС:\s*\S*', line)[0].split()[-1])
                elif findall(r'Код продукта:\s*\S*', line):
                    os_code_list.append(findall(r'Код продукта:\s*\S*', line)[0].split()[-1])
                elif findall(r'Тип системы:\s*\S*', line):
                    os_type_list.append(findall(r'Тип системы:\s*\S*', line)[0].split()[-1])
    main_data.extend([os_prod_list, os_name_list, os_code_list, os_type_list])
    return main_data


def write_to_csv(file, main_data):
    with open(file, mode="w", newline='') as file_n:
        w = DictWriter(file_n, fieldnames=main_data[0], dialect="excel-tab")
        w.writeheader()
        for i in range(3):
            w.writerow({" ": str(i + 1),
                        "Изготовитель системы": main_data[1][i],
                        "Название ОС": main_data[2][i],
                        "Код продукта": main_data[3][i],
                        "Тип системы": main_data[4][i]})


result = get_data(['info_1.txt', 'info_2.txt', 'info_3.txt'])
write_to_csv("main_data.csv", result)
with open("main_data.csv") as f_n:
    print(f_n.read())
