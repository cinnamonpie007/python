from random import randint

# lesson1


def square():
    wight = int(input('Ширина : '))
    height = int(input('Высота : '))

    for i in range(height):
        if i == 0:
            print('|', '-' * wight, '|', end='\n')
        elif i != 0 and i != (height - 1):
            print('|', ' ' * wight, '|', end='\n')
        elif i == (height - 1):
            print('|', '-' * wight, '|', end='')


# square()


def trigon():
    x = int(input('a : '))
    y = int(input('b : '))
    z = int(input('c : '))

    if x <= (y + z) and y <= (x + z) and z <= (x + y):

        print("Треугольник существует.")

        if x == y == z:
            print("Треугольник равносторонний.")

        elif x == y or y == z or x == z:
            print("Треугольник равнобедренный.")

        else:
            print("Треугольник разносторонний.")

    else:
        print("Треугольник не существует.")


# trigon()


def prime_numbers():
    x = int(input('сколько чисел проверяем : '))
    numbs = []
    count_numbs = 0

    while x > 0:
        y = int(input('введите число : '))
        z = 0
        for i in range(1, y + 1):
            if y % i == 0 and y != 1:
                z += 1
            elif y == 1:
                count_numbs += 1
                numbs.append(y)
            else:
                pass
        if z == 2:
            numbs.append(y)
            count_numbs += 1
        else:
            pass

        x -= 1

    print(numbs, end='\n')
    print(count_numbs)


prime_numbers()

# x = 5
# str_count = x
# lines = []
#
#
# for i in range(str_count):
#     xx = []
#     for j in range(1, str_count - i):
#         xx.append(j)
#         continue
#
#     print('.' * len(xx), xx[-1])
#


def random_numb():
    min_n = 1
    max_n = 100

    while True:
        n = randint(min_n, max_n)

        print(f'Ваше число {n} ?')

        print('1 - Угадал\n2 - Больше\n3 - Меньше')
        print(max_n, min_n)
        x = int(input('dsfsd: '))

        if x == 1:
            print('Ураааа !!!')
            break

        elif x == 2:
            min_n = n
            continue

        elif x == 3:
            max_n = n


random_numb()