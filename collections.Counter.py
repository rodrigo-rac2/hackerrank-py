# Enter your code here. Read input from STDIN. Print output to STDOUT
# Problem: https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
# 
from collections import Counter


def calculateEarnings():
    earnings = 0
    shoe_number = input()
    shoe_sizes = Counter(input().split())
    for i in range(int(input())):
        desired_size, value = input().split()
        if shoe_sizes[desired_size] > 0:
            earnings = earnings + int(value)
            shoe_sizes[desired_size] = shoe_sizes[desired_size] - 1
    return earnings


if __name__ == "__main__":
    print(calculateEarnings())
