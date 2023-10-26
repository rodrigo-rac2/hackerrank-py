import string


def calc_width(size):
    if size == 1:
        return 1
    return calc_width(size-1) + 4


def get_first_half(index, size, width):
    chars_to_print = []
    for i in range(size - index):
        chars_to_print.append(string.ascii_lowercase[size - 1 - i])

    result_unfilled = '-'.join(chars_to_print) + '-'

    half = (width - 1) // 2
    empty_spaces = half - len(result_unfilled)

    return ('-' * empty_spaces).ljust(empty_spaces) + result_unfilled


def get_second_half(index, size, width):
    chars_to_print = []
    for i in range(size - index, 0, - 1):
        chars_to_print.append(string.ascii_lowercase[size - i])

    result_unfilled = '-' + '-'.join(chars_to_print)

    half = (width - 1) // 2
    empty_spaces = half - len(result_unfilled)

    return result_unfilled + ('-' * empty_spaces).rjust(empty_spaces)


def print_rangoli(size):
    if size == 1:
        print('a')
        return
    width = calc_width(size)
    for i in range(size, 0, -1):
        print(get_first_half(i, size, width) + string.ascii_lowercase[i - 1] + get_second_half(i, size, width))

    for i in range(2, size + 1, 1):
        print(get_first_half(i, size, width) + string.ascii_lowercase[i - 1] + get_second_half(i, size, width))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)