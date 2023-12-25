# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

string_a = input()
string_b = input()
set_a = list(map(int, string_a.split(' ')))
set_b = list(map(int, string_b.split(' ')))
result_l = product(set_a, set_b)
result_s = ''

for elem in result_l:
    num_list = [str(num) for num in elem]
    tuple_s = ", ".join(num_list)
    result_s = result_s + f"({tuple_s}) "
            
print(result_s)
