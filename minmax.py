arr = [5, 5, 5, 5, 5]

max_value = 0
min_value = 1000000001

max_sum = 0
min_sum = 0

array_max_sum = []
array_min_sum = []

for num in arr:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

double_min = False
double_max = False

i = 0
while i < len(arr):
    if (arr[i] != min_value) or double_min:
        array_max_sum.append(arr[i])
    else:
        double_min = True
    if (arr[i] != max_value) or double_max:
        array_min_sum.append(arr[i])
    else:
        double_max = True
    i = i + 1

for max_e in array_max_sum:
    max_sum = max_sum + max_e
for min_e in array_min_sum:
    min_sum = min_sum + min_e


print([min_sum, max_sum])

#print(min_sum)