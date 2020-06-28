revenue = int(input("Ваша выручка?"))
cost = int(input("Ваши издержки?"))
rev_cost = revenue - cost
if rev_cost > 0:
    print('Ваша прибыль ', (rev_cost))
    print('Рентабельность выручки', round(rev_cost/revenue, 2))
    personal = int(input("Сколько людей на вас работает?"))
    print('Прибыль на одного сотрудника ', round(rev_cost/personal, 2))
else:
    print('Вашы убытки ', (abs(rev_cost)))