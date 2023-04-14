"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
from chardet import detect
from urllib.request import urlopen

yan = urlopen('http://yandex.ru/').read()
print(detect(yan))

yt = urlopen('http://youtube.com/').read()
print(detect(yt))
