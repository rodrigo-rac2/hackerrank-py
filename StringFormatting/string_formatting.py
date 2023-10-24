def print_formatted(number):
    spaces = len(format(number, 'b'))
    for i in range(1, int(number) + 1):
        integer = format(i, 'd')
        octal = format(i, 'o')
        hexa = format(i, 'X')
        binary = format(i, 'b')
        i_separator = " " * (spaces - len(integer))
        o_separator = " " * (spaces - len(octal) + 1)
        h_separator = " " * (spaces - len(hexa) + 1)
        b_separator = " " * (spaces - len(binary) + 1)
        print(i_separator + integer +
              o_separator + octal +
              h_separator + hexa +
              b_separator + binary)

    # width = len(bin(number)[2:])
    # print("{0:>{width}d} {1:>{width}o} {2:>{width}X} {3:>{width}b}".format(i,i,i,i,width=width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
