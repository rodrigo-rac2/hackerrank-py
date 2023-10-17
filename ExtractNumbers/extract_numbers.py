import re
import numpy as np


def return_numbers(text):
    array_text = [char for char in text]
    return_numbers = []
    i = 0
    while i < len(array_text):
        candidate_number = ''
        if array_text[i].isdigit():
            while array_text[i].isdigit():
                candidate_number += array_text[i]
                i += 1
            if array_text[i] == '.':
                candidate_number += array_text[i]
                i += 1
                while array_text[i].isdigit():
                    candidate_number += array_text[i]
                    i += 1
                return_numbers.append(float(candidate_number))
            else:
                return_numbers.append(int(candidate_number))
        i += 1
    return return_numbers
    # numbers = list(filter(lambda x: x.isdigit(), text.split()))
    # return [int(s) for s in numbers]


if __name__ == '__main__':
    txt1 = "sdfhj1jdh12sjfh123jhsf12.1skdj"

    print(return_numbers(txt1))
