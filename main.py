while True:
    try:
        a = int(input("Введите целое число: "))
        print("Вы ввели целое число", a)
        break
    except ValueError:
        print("Невозможно преобразовать введенное значение в целое число. Введите число еще раз.")
    except TypeError:
        print()