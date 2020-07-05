my_sting = input("Введите что-нибудь").split()
for i, word in enumerate(my_sting, start=1):
    print(i, word[:10])