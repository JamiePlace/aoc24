from collections import deque
import operator

def read_file():
    with open("./run/day2_1.txt", 'r') as file:
        data = file.readlines()
    data = list(map(lambda x: x.replace("\n", ""), data))
    data = list(map(lambda x: x.split(" "), data))
    data = list(map(lambda x: list(map(lambda y: int(y), x)), data))
    return data

def decrease_increase_check(diff):
    base_sum = sum(diff)
    pos_sum = sum(list(map(lambda x: (x**2)**0.5, diff)))
    if pos_sum == base_sum:
        return True
    if pos_sum == -1 * base_sum:
        return True
    return False

def part1():
    data = read_file()
    report_classification = []
    for report in data:
        print('report class', report_classification)
        print('report', report)
        diff = list(map(operator.sub, report, report[1::]))
        if not decrease_increase_check(diff):
            report_classification.append(0)
            continue
        
        abs_diff = list(map(abs, diff))
        print('abs_diff', abs_diff)
        if max(abs_diff) <= 3 and max(abs_diff) >= 1 and min(abs_diff) >= 1 and min(abs_diff) <= 3:
            report_classification.append(1)
            continue
        report_classification.append(0)
        
    print(report_classification)
    print(sum(report_classification))

def part2():
    pass
    
if __name__ == "__main__":
    part1()
    part2()

