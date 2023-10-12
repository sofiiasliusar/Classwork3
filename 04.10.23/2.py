def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
while True:
    print("1.Цельсія в Фаренгейт")
    print("2.Фаренгейт в Цельсія")
    print("3.Вийти")
    choice = input("Оберіть 1, 2, 3: ")
    if choice == "1":
        celsius = float(input("Введіть температуру в градусах Цельсія: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} градусів Цельсія дорівнює {fahrenheit} градусів за Фаренгейтом.")
    elif choice == "2":
        fahrenheit = float(input("Введіть температуру в градусах за Фаренгейтом: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print (f"{fahrenheit} градусів за Фаренгейтом дорівнює {celsius} градусів Цельсія.")
    elif choice == "3":
        break
    else:
        print("")
   