if __name__ == '__main__':
    poems = [len([j for j in i if j in 'аеёиоуыэюя']) for i in input().lower().split()]
    print('Парам пам-пам') if len(set(poems)) == 1\
        else print('Пам парам')
