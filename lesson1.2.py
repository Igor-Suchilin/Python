time = int(input("Введите время в секундах"))
hour = time // 3600
time = time - hour * 3600
minute = time // 60
second = time - minute * 60
print(f"{hour}ч:{minute}м:{second}с")
