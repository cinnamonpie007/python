
def double(word):
    result = ''
    if len(word) > 1:
        last_simb = ''
        for i in word:
            if last_simb == i:
                result += i
                last_simb = i
            else:
                last_simb = i
    else:
        return word
    return result


if __name__ == '__main__':
    result = double()

