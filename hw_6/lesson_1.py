def dicts(list_word):
    words = {}
    for i in list_word:
        i = str(i).replace(' ', '')
        if i in words.keys():
            count = words.get(i)
            words[i] = count + 1
        else:
            words[i] = 1
    return words


if __name__ == '__main__':
    modul_dict = dicts()

