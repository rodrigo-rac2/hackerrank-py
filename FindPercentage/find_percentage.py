def read_input():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    return student_marks


def get_average(student_marks, query_name):
    return sum(student_marks[query_name]) / len(student_marks[query_name])


if __name__ == '__main__':
    student_marks = read_input()
    query_name = input()
    print("%.2f" % get_average(student_marks, query_name))
