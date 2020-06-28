def choose_plural(num, choice):
    if (num // 10) % 10 == 1 or num % 10 == 0:
        return str(num) + ' ' + choice[2]
    elif num % 10 == 1:
        return str(num) + ' ' + choice[0]
    elif num % 10 <= 4:
        return str(num) + ' ' + choice[1]
    else:
        return str(num) + ' ' + choice[2]

choice = 'день дня дней'.split()
a = int(input('Сколько киллометров пробежали в первый день?'))
b = int(input('Сколько киллометров хотите пробежать'))
days = 12
if a >= b:
    print("Нужно хотеть больше!")
while a <= b:
    a += (a/10)
    days += 1
print('Через', choose_plural(days, choice), 'вы пробежите сколько хотите')