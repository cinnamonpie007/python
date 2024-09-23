from lesson_1 import dicts
from lesson_2 import double
from lesson_3 import uniq
from lesson_4 import dates
from lesson_5 import queen


def lesson_1():
    words = input('слова : ').split(',')
    return dicts(words)


def lesson_2():
    words = input('символы : ')
    return double(words)


def lesson_3():
    list_1 = input('значения 1 : ').split(',')
    list_2 = input('значения 2 : ').split(',')
    return uniq(list_1, list_2)


def lesson_4():
    date_char = input('Введите дату в формате DD.MM.YYYY : ').split('.')
    if len(date_char) == 3:
        return dates(date_char[0], date_char[1], date_char[2])
    else:
       return "Ошибка формата даты"


def lesson_5():
    return queen


print(lesson_5())

# print(lesson_4())

# print(lesson_3())

# print(lesson_2())

# print(lesson_1())


