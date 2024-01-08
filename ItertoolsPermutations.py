# Enter your code here. Read input from STDIN. Print output to STDOUT
# Problem: https://www.hackerrank.com/challenges/itertools-permutations/

from itertools import permutations

print_list = []
S, k = input().split()
for _tuple in list(permutations(S, int(k))):
    s = ''
    for char in _tuple:
        s = s + char
    print_list.append(s)
print_list.sort()
for permutation in print_list:
    print(permutation)
