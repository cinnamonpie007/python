# lesson 1
import random


def sum_numb(numb1):
    numb = numb1
    result = 0
    while numb > 0:
        result += numb % 10
        numb //= 10
    return result

def max_num(numb1):
    numb = numb1
    result = 0
    while numb > 0:
        if numb % 10 > result:
            result = numb % 10
        numb //= 10
    return result

def min_num(numb1):
    numb = numb1
    result = numb % 10
    while numb > 0:
        if numb % 10 < result:
            result = numb % 10
        numb //= 10
    return result


def run_lesson1():
    while True:
        numb = int(input('введите число : '))
        what_do = int(input('что сделать ? : '))
        if what_do == 1:
            print(sum_numb(numb))
        elif what_do == 2:
            print(max_num(numb))
        elif what_do == 3:
            print(min_num(numb))
        elif what_do == 0:
            break


def rock_paper_scissors():
    chose_dict = {
        1: 'Камень',
        2: 'Ножницы',
        3: 'Бумага'
    }
    while True:
        print('1 - Камень, 2 - Ножницы, 3 - Бумага, 0 - выход')
        human_val = int(input('введите число : '))
        chose_pc = list(chose_dict.keys())
        pc_val = random.choice(chose_pc)
        if human_val == 0:
            break
        elif 3 > int(human_val) < 0:
            print('значение неизвестно')
        else:
            if human_val + pc_val == 3 and human_val != pc_val:
                if human_val < int(pc_val):
                    print('Победа человека')
                else:
                    print('Победа компьютера')
            elif human_val + pc_val == 4 and human_val != pc_val:
                if human_val > pc_val:
                    print('Победа человека')
                else:
                    print('Победа компьютера')
            elif human_val + pc_val == 5 and human_val != pc_val:
                if human_val < pc_val:
                    print('Победа человека')
                else:
                    print('Победа компьютера')
            elif human_val == pc_val:
                print('Ничья')

def guess_the_number():
    pc_chose = random.randint(0, 100)
    print("Попробуй угадать число, которое загадал ПК")
    while True:
        human_chose = int(input("Введите число : "))
        if human_chose > pc_chose:
            print('ПК загадал число меньше')
        elif human_chose < pc_chose:
            print('ПК загадал число больше')
        elif human_chose == pc_chose:
            print("Ты угадал")
            break

def mainMenu():
    x = int(input('во что играем : '))
    if x == 1:
        rock_paper_scissors()
    elif x == 2:
        guess_the_number()


def numb_revers():
    numb_1 = input("Число 1 : ")
    numb_2 = input("Число 2 : ")
    numb_1_rev = list(numb_1)
    numb_2_rev = list(numb_2)
    n1 = reversed(numb_1_rev)
    n2 = reversed(numb_2_rev)
    numb_1_rev_1 = ''.join(n1)
    numb_2_rev_2 = ''.join(n2)

    print(f'Первое число: {int(numb_1)}')
    print(f'Второе число: {int(numb_2)}')
    print(f'Сумма: {int(numb_1) + int(numb_2)}')
    print(f'Первое число наоборот: {int(numb_1_rev_1)}')
    print(f'Первое число наоборот: {int(numb_2_rev_2)}')
    print(f'Сумма наоборот: {int(numb_1_rev_1) + int(numb_2_rev_2)}')


def max_of_2(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


def max_of_3(num1, num2, num3):
    numb1 = max_of_2(num1, num2)
    result = max_of_2(numb1, num3)
    return result


def func_max():
    digit_1 = int(input('Введите первое число: '))
    digit_2 = int(input('Введите второе число: '))
    digit_3 = int(input('Введите третье число: '))
    result = max_of_3(digit_1, digit_2, digit_3)
    return f'максимальное число из {digit_1}, {digit_2}, {digit_3} является {result}'


def calculate_danger(x):
    return x**3 - 3 * x**2 - 12 * x + 10


def find_safe_depth(max_danger):
    d_min = 0
    d_max = 4
    d_middle = (d_min + d_max) / 2
    middle_danger = calculate_danger(d_middle)

    while abs(middle_danger) > max_danger:
        if middle_danger > 0:
            d_min = d_middle
        else:
            d_max = d_middle
        d_middle = (d_min + d_max) / 2
        middle_danger = calculate_danger(d_middle)
    return d_middle


def main():
    max_danger = float(input('Введите допустимый уровень опасности: '))
    if max_danger < 0:
        print('Вы ввели недопустимое значение! Попробуйте еще раз.')
    else:
        safe_depth = find_safe_depth(max_danger)
    print(f'Приблизительная глубина безопасной кладки:{safe_depth: .9f} м')


main()

# print(func_max())

# numb_revers()

# mainMenu()

# run_lesson1()


