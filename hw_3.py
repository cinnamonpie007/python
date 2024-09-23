import random
import string


# lesson 1

def duble():
    elements = [1, 2, 2, 2, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 2, 3]

    double = list()

    for i in elements:
        if i not in double:
            double.append(i)

    return double


def max_num():
    input_numb = input('введите список : ').split()
    numb = [int(i) for i in input_numb]

    max_numb = numb[0]

    for i in numb:
        if i > max_numb:
            max_numb = i

    return max_numb


def polindrom():
    input_str = input('введите строку : ').lower()
    new_str = ''
    len_str = list(input_str)
    while len(len_str) > 0:
        x = len_str.pop()
        new_str += x

    if new_str == input_str:
        result = 'полиндром'
    else:
        result = 'не полиндром'

    return result


def password():
    pwd_len = int(input('введите длину пароля : '))
    pwd_str = string.ascii_letters
    pwd_int = string.digits
    pwd_char = ".,:;!_*-+()/#¤%&)\"'|"
    pwd_join = pwd_str + pwd_int + pwd_char
    pwd = []
    while len(pwd) < pwd_len:
        pwd.append(random.choice(pwd_join))
    return ''.join(pwd)


def anagram():
    word_1 = 'кулон'
    word_2 = 'клосн'

    if len(word_1) != len(word_2):
        return 'Слова не являются анаграммами'

    else:
        dict_1 = {}
        dict_2 = {}

        for i in word_1:
            if i in dict_1.keys():
                dict_1[i] += 1
            else:
                dict_1[i] = 1

        for i in word_2:
            if i in dict_2.keys():
                dict_2[i] += 1
            else:
                dict_2[i] = 1

        if dict_1 == dict_2:
            return 'анаграммы'
        else:
            return 'не анаграммы'





# print(anagram())

# print(password())

# print(polindrom())


# print(max_num())

# print(duble())