from datetime import date


def dates(d, m, y):
    leap_year = leap_years(y)
    day_input = int(d)
    month_input = int(m)
    year_input = int(y)

    if day_input < 1 or day_input > 31:
        return 'Такого дня не существует'
    if month_input < 1 or month_input > 12:
        return 'Такого месяца не существует'
    if year_input < 1 or year_input > 9999:
        return 'Такого года не существует'

    if month_input in [4, 6, 9, 11] and day_input > 30:
        return 'В этом месяце не может быть больше 30 дней'
    if month_input == 2:
        if leap_year and day_input > 29:
            return 'В феврале не может быть столько дней'
        elif not leap_year and day_input > 28:
            return 'В феврале в высокосный год не может быть столько дней'

    if date(year=year_input, month=month_input, day=day_input):
        return "Дата валидна"
    else:
        return "Дата не валидна"


def leap_years(y):
    year_input = int(y)
    if (year_input % 4 == 0 and year_input % 100 != 0) or (year_input % 400 == 0):
        return True
    else:
        return False
