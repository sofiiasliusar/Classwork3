def conversion():
    print("Ви хочете перевести \n1.З Цельсія у Фаренгейт \n2.З Фаренгейт у Цельсія")
    convert = input("?")
    if convert == "1":
        c = float(input("Вкажіть градуси у Цельсіях: "))
        f = (int(c) * 9/5) + 32
        print(f"{c} градусів Цельсія дорівнює {f} градусів за Фаренгейтом.")
    elif convert == "2":
        f = float(input("Вкажіть градуси за Фаренгейтом: "))
        c = (int(f) - 32) * 5/9
        print(f"{c} градусів за Фаренгейтом дорівнює {f} градусів Цельсія.")
    else:
        conversion()
conversion()