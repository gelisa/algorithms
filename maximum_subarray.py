# Elizaveta Guseva, 2018


def max_subarray_kadane(arr):
    if len(arr) == 1:
        return arr[0]

    max_at_position = arr[0]
    max_so_far = arr[0]
    for item in arr[1:]:
        max_at_position = max(item, max_at_position + item)
        max_so_far = max(max_at_position, max_so_far)
    return max_so_far


