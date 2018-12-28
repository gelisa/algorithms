# Elizaveta Guseva, 2018


def find_string_bf(string, query):
    locations = []
    for (i, s) in enumerate(string):
        for (j, qs) in enumerate(query):
            if qs != string[i+j]:
                break
        else:
            locations.append(i)
    return locations




