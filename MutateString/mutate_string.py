def mutate_string(string, position, character):
    result_string = ''
    index = 0
    while index < len(string):
        if index == position:
            result_string = result_string + character
        else:
            result_string = result_string + string[index]

        index = index + 1
    return result_string

# def mutate_string(string, position, character):
#     return string[:position] + character + string[position+1:]


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
