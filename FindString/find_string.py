# def count_substring(string, sub_string):
#     counter = 0
#     i = 0
#     while i < len(string):
#         if len(string[i:]) < len(sub_string):
#             break
#         if string[i] == sub_string[0]:
#             j = 0
#             while j < len(sub_string):
#                 if string[i + j] != sub_string[j]:
#                     break
#                 j = j + 1
#             if j == len(sub_string):
#                 counter = counter + 1
#         i = i + 1
#     return counter


def count_substring(string, sub_string):
    counter = 0
    sub_len = len(sub_string)

    for s1 in range(0, len(string)):
        if string[s1:s1 + sub_len] == sub_string:
            counter += 1
    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
