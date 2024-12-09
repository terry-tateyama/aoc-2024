import sys
sys.path.append("play/aoc-2024/")
from common import *

###############################################################################
# CODE
###############################################################################

def parse_report(line):                                 # " 15    16    19    20    23    26    27"
    list_of_strings = line.split()                      # ['15', '16', '19', '20', '23', '26', '27']
    return [int(data) for data in list_of_strings]      # [ 15,   16,   19,   20,   23,   26,   27]

def is_safe(data_list):
    is_in_range = True
    is_ascending = True
    is_descending = True
    prev = data_list[0]
    for next in data_list[1:]:
        is_in_range = is_in_range and (abs(prev - next) <= 3)
        is_ascending = is_ascending and (prev < next)
        is_descending = is_descending and (prev > next)
        prev = next
    return (is_ascending or is_descending) and is_in_range

def part1_calc(reports):
    number_of_safe_reports = 0
    for line in reports:
        if  is_safe(parse_report(line)):
            number_of_safe_reports += 1
    return  number_of_safe_reports

def is_safe_without_an_element(data_list):
    for ii in range(0, len(data_list)):             # index of each element in report
        reduced_list = copy.deepcopy(data_list)
        reduced_list.pop(ii)                        # compute  list without element
        if is_safe(reduced_list):                   # evaluate list without element
            return True                             # we only need one "safe" arrangement
    return False                                    # could not find "safe" arrangement

def part2_calc(reports):
    number_of_safe_reports = 0
    for line in reports:
        if  is_safe_without_an_element(parse_report(line)):
            number_of_safe_reports += 1
    return  number_of_safe_reports

###############################################################################
# RUNNING
###############################################################################
day   = 2
lines = get_input(f'play/aoc-2024/{day:02}/practice.txt')
check_aoc(day, 'practice part 1', part1_calc(lines), 2)
check_aoc(day, 'practice part 2', part2_calc(lines), 4)

lines = get_input(f'play/aoc-2024/{day:02}/real.txt')
check_aoc(day, 'for real part 1', part1_calc(lines), 314)
check_aoc(day, 'for real part 2', part2_calc(lines), 373)