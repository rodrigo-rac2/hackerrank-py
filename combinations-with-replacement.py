# Problem: https://www.hackerrank.com/challenges/itertools-combinations-with-replacemen

from itertools import combinations_with_replacement



if __name__ == '__main__':
    S, k = input().split()
    for t in combinations_with_replacement(''.join(sorted(list(S))), int(k)):
        for element in t:
            print(element, end='')
        print()
