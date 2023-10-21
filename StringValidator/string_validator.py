if __name__ == '__main__':
    s = input()
    print(any(x.isalnum() for x in s))
    print(any(x.isalpha() for x in s))
    print(any(x.isdigit() for x in s))
    print(any(x.islower() for x in s))
    print(any(x.isupper() for x in s))
# hasAlfNum, hasAlfa, hasDigit, hasLower, hasUpper = False, False, False, False, False
# for c in s:
#     if c.isalnum():
#         hasAlfNum = True
#         if c.isalpha():
#             hasAlfa = True
#             if c.islower():
#                 hasLower = True
#             elif c.isupper():
#                 hasUpper = True
#         elif c.isdigit():
#             hasDigit = True
#
# print(f'{hasAlfNum}\n{hasAlfa}\n{hasDigit}\n{hasLower}\n{hasUpper}')
