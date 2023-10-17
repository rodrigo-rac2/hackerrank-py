import operator
from typing import List, Any

def find_second_lowest_grade(ordered_grades):
    lowest_grade = min(ordered_grades)
    for i in range(len(ordered_grades)):
        if ordered_grades[i] > lowest_grade:
            return ordered_grades[i]


def get_second_lowest_score_student_name(records):
    second_lowest_score_list = []
    sorted_records = dict(sorted(records.items(), key=lambda x: x[1], reverse=False))
    sorted_records_list = list(sorted_records.items())
    second_lowest_grade = find_second_lowest_grade(list(sorted_records.values()))
    for i in range(len(sorted_records_list)):
        if sorted_records_list[i][1] == second_lowest_grade:
            second_lowest_score_list.append(sorted_records_list[i][0])
    return sorted(second_lowest_score_list)


if __name__ == '__main__':
    records = dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records[name] = score

    second_lowest_score_list = get_second_lowest_score_student_name(records)
    for student in second_lowest_score_list:
        print(student)
