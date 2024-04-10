def udacha(n):
    if len(n) % 2 != 0:
        return False
    n_one = sum(
        map(int, n[: len(n) // 2])
    )  # оставлю тут, чтобы не забыть, "map" для того, чтобы присваивать к каждому элементу списка
    n_two = sum(
        map(int, n[len(n) // 2 :])
    )  # оставлю тут, чтобы не забыть, ":" для срезы, чтоб делить строку
    return n_one == n_two


ticket = input(f"Номер билета: ")
if udacha(ticket):
    print(f"Счастливый билет")
else:
    print(f"Не счастливый билет")
