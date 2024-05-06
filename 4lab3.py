def magic(date):
    try:
        day, month, year = map(int, date.split("."))  # оставлю тут, split это разделитель
        return day * month == year % 100
    except ValueError:
        return False


userdate = input(f"Дата через точку ")
if magic(userdate):
    print(f"Магическая дата")
else:
    print(f"Не магическая дата")
