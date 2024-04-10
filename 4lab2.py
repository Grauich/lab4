def delenie(n):
    try:
        N = 100 / n
        return N
    except ValueError:
        return "Ошибка: Введена строка"
    except ZeroDivisionError:
        return "Ошибка: Введен ноль"


def main():
    user = input(f"Введите число для деления 100 ")
    try:
        n = float(user)
        N = delenie(n)
        print(f"{N}")
    except ValueError:
        print(f"Ошибка: Введена строка")


main()
