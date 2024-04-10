def delenie(n):
    return n % 3 == 0


n = int(input("Введите число: "))
if delenie(n):
    print(f"{n} делится на 3")
else:
    print(f"{n} не делится на 3")
