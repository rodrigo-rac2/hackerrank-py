# Problem: https://www.hackerrank.com/challenges/symmetric-difference/

def sym_diff_print(set_a, set_b):
    element_l = []
    union_set = set_a.union(set_b)
    intersect_set = set_a.intersection(set_b)
    for element in union_set:
        if element not in intersect_set:
            element_l.append(element)
    element_l.sort()
    for element in element_l:
        print(element)


if __name__ == '__main__':
    input()
    set_a = set(map(int, input().split()))
    input()
    set_b = set(map(int, input().split()))
    sym_diff_print(set_a, set_b)
