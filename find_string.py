# Elizaveta Guseva, 2018


def find_string_bf(string, query):
    if query == '':
        return []

    locations = []
    ls = len(string)
    for (i, s) in enumerate(string):
        for (j, qs) in enumerate(query):
            if (i+j < ls) and (qs != string[i+j]):
                break
            elif i+j >= ls:
                break
        else:
            locations.append(i)
    return locations




