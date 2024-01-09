# Enter your code here. Read input from STDIN. Print output to STDOUT
#
# Problem: https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations


def print_sorted_combinations(S, k):
    for i in range(k):
        comb = list(combinations(''.join(sorted(S)), i + 1))
        for value in comb:
            for c in value:
                print(c, end="")
            print()


if __name__ == '__main__':
    S, k = input().split()
    print_sorted_combinations(S, int(k))
