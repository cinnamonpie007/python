def uniq(list_1, list_2):
    set_1 = set(list_1)
    set_2 = set(list_2)
    set_list = (set_2 - set_1) | (set_1 - set_2)
    result = list(set_list)
    return list(result)
