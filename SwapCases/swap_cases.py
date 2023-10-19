def swap_case(s):
    array_s = [char for char in s]
    result_string = ''
    for c in array_s:
        if c.islower():
            result_string = result_string + c.upper()
        else:
            result_string = result_string + c.lower()
    return result_string


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
