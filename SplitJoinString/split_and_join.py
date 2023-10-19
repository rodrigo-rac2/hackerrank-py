def split_and_join(line_str):
    return "-".join(line_str.split())


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)