
def sort_by_len_asc(s1, s2):
    if len(s1) >= len(s2):
        return s1, s2
    else:
        return s2, s1


def sum_digits(digit1, digit2):
    raw_sum = int(digit1) + int(digit2)
    carry = str(raw_sum // 2)
    position_sum = str(raw_sum % 2)
    return position_sum, carry

def table_binary_addition(s1, s2):
    output = ''
    carry = 0
    long, short = sort_by_len_asc(s1, s2)
    l_len = len(long)
    s_len = len(short)
    for i in range(l_len):
        if i >= s_len:
            position_sum, carry = sum_digits(long[l_len - i - 1], carry)
        else:
            position_sum, carry = sum_digits(long[l_len - i - 1], short[s_len - i - 1])
        output = '{}{}'.format(position_sum, output)

    return '{}{}'.format(carry, output).lstrip('0')



