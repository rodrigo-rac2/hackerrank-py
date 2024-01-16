# problem: https://www.hackerrank.com/challenges/compress-the-string/
from itertools import groupby

l = []
for k,v in groupby(input()):
    l.append((len(list(v)),int(k)))
print(*l)

# for k,v in groupby(input()):
    # print (f'({len(list(v))}, {k})', end=" ")
