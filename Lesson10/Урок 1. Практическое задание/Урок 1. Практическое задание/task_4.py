"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
words = ['разработка', 'администрирование', 'protocol', 'standard']
byte_format = [item.encode('utf-8') for item in words]
str_format = [item.decode('utf-8') for item in byte_format]
print(byte_format)
print(str_format)
