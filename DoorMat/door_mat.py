
def print_door_mat(n, m):
    for i in range(n):
        if i == n // 2:
            print('WELCOME'.center(m, '-'))
        elif i < n // 2:
            print(('.|.' * (2 * i + 1)).center(m, '-'))
        else:
            print(('.|.' * (2 * (n - i - 1) + 1)).center(m, '-'))


if __name__ == '__main__':
    s = input()
    n, m = s.split()
    print_door_mat(int(n), int(m))