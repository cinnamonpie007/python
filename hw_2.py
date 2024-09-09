# lesson 1

def nod():
    nod_num_1 = int(input("число 1 : "))
    nod_num_2 = int(input("число 2 : "))

    min_n = min(nod_num_1, nod_num_2)
    max_n = max(nod_num_1, nod_num_2)
    result = found_max(min_n, max_n)
    return result


def found_max(mins, maxs):
    while mins:
        mins, maxs = maxs % mins, mins

    return maxs


# lesson_2

def hex_numbs():
    numbs = int(input('введите число : '))
    hex_digits = '0123456789abcdef'
    hex_string = str()
    is_negative = numbs < 0

    if numbs == 0:
        hex_string = str(0)

    else:
        num = numbs
        if is_negative:
            num = numbs * -1
        while num > 0:
            remainder = num % 16
            hex_string = str(hex_digits[remainder]) + str(hex_string)
            num //= 16

    if is_negative:
        hex_string = '-' + hex_string

    return hex_string, hex(numbs)

# lesson_3


def rome_numb():
    num = int(input("Введите целое число: "))
    num_arabian = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    num_rom = syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    result = ''

    i = 0

    while num > 0:
        for _ in range(num // num_arabian[i]):
            result += num_rom[i]  # Добавляем соответствующий римский
            num -= num_arabian[i]  # Уменьшаем значение num на val[i]
        i += 1

    return result





# print(rome_numb())

# print(hex_numbs())

# print(nod())


