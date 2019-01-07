# Elizaveta Guseva, 2019

import queue


def wb_dyn_prog(string: str, word_dict: set):
    answ_arr = [1] + [0] * len(string)
    for substr_len in range(1, len(string) + 1):
        for break_point in range(substr_len):
            if answ_arr[break_point]:
                if string[break_point:substr_len] in word_dict:
                    answ_arr[substr_len] = True
                    break

    return answ_arr[-1]


def wb_bfs(string: str, word_dict: set):
    q = queue.Queue()
    start = 0
    q.put(start)
    visited = [0] * len(string)
    while not q.empty():
        start = q.get()
        if visited[start] == 0:
            for j in range(start+1, len(string)+1):
                if string[start:j] in word_dict:
                    if j == len(string):
                        return True
                    q.put(j)

            visited[start] = 1

    return False



