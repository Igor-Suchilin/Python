month = (int(input('Введите номер месяца'))) % 12
month_list = ("Зима", "Весна", "Лето", "Осень")
print(month_list[(month // 3)])
month_tuple = {0: "Зима", 1: "Весна", 2: "Лето", 3: "Осень"}
print(month_tuple[month // 3])