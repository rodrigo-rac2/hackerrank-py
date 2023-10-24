import textwrap

def wrap(string, max_width):
    result_string = ""
    for i in range(len(string)):
        if i % max_width == 0 and i > 0:
            result_string = result_string + "\n" + string[i]
        else:
            result_string = result_string + string[i]
    return result_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
