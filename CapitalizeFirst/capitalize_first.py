#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    for i in range(len(s)):
        if i == 0 or (i != ' ' and s[i - 1] == ' '):
            s = s[:i] + s[i].upper() + s[i + 1:]
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
