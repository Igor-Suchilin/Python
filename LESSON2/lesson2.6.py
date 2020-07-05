goods = []
spisok = {'название': '', "цена": '', 'количество':'', 'единица измерения':''}
analitics = {'название': [], "цена": [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input().upper() == 'Q':
        break
    num += 1
    for f in spisok.keys():
        user_data = input('{}: '.format(f))
        spisok[f] = int(user_data) if (f == 'цена' or f == 'количество') else user_data
        analitics[f].append(spisok[f])
    goods.append((num, spisok.copy()))
    print('Текущая аналитика по товарам:\n')
    for key, value in analitics.items():
        print(key, value)