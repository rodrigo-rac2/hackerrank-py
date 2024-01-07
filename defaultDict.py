# Enter your code here. Read input from STDIN. Print output to STDOUT

# Problem: https://www.hackerrank.com/challenges/defaultdict-tutorial/

from collections import defaultdict


def main():
    a = defaultdict(list)

    n, m = map(int, input().split())

    for i in range(n):
        a[input()].append(i + 1)
    for j in range(m):
        b = input()
        if b in a:
            print(*a[b], ' ')
        else:
            print('-1')


if __name__ == '__main__':
    main()
