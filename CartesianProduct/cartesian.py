# Enter your code here. Read input from STDIN. Print output to STDOUT
string_a = input()
string_b = input()
set_a = list(map(int, string_a.split(' ')))
set_b = list(map(int, string_b.split(' ')))
result_l = []
result_s = ''

for number_set_a in set_a:
    for number_set_b in set_b:
        # tuple_a = (number_set_a, number_set_b)
        # tuple_b = (number_set_b, number_set_a)
        # if (tuple_a not in result_l) and (tuple_b not in result_l):
            tuple_s = f'({number_set_a}, {number_set_b}) '
            result_s = result_s + tuple_s
            # result_l.append(tuple_a)
            
print(result_s)
