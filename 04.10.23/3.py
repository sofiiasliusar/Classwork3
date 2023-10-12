
def guess_number():
    number = input("Вгадайте число! Від 1 до 90: ")
    if number == "88":
        print("Правильно! Вітаю!")
    elif number < "88":
        print("Спробуйте ввести більше число!")
        guess_number()
    elif number > "88":
        print("Спробуйте ввести менше число!")
        guess_number()
    else:
        print("Неправильно! Введіть число в заданих межах!")
        guess_number()
guess_number()
