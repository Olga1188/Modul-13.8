ticket = int(input("Введите количество билетов "))
money = 0
for i in range(ticket):
    age = int(input("Возраст: "))
    if age < 18:
        money = money + 0
    elif 18 <= age < 25:
        money = money + 990
    else:
        money = money + 1390
    if ticket > 3:
        money = money * 0.9
print("Итого:" + " " + str(round(money)) + " " + "рублей")