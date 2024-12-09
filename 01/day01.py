import sys
sys.path.append("play/aoc-2024/")
from common import *

###############################################################################
# CODE
###############################################################################
def parse_input(lines):
    list1 = []
    list2 = []
    for line in lines:
        x, y = line.split()
        list1.append(int(x))
        list2.append(int(y))
    return list1, list2

def sort_and_compute_diffs(list1, list2):
    list1.sort()
    list2.sort()
    diff_list = []
    for x,y in zip(list1, list2):
        diff_list.append(abs(x-y))
    return diff_list

def part1_calc(lines):
    list1, list2 = parse_input(lines)
    diff_list = sort_and_compute_diffs(list1, list2)
    return sum(diff_list)

def part2_calc(lines):
    list1, list2 = parse_input(lines)
    running_total = 0
    for item in list1:
        counts = list2.count(item)
        running_total += item * counts
    return running_total

###############################################################################
# RUNNING
###############################################################################
day   = 1
lines = get_input(f'play/aoc-2024/{day:02}/practice.txt')
check_aoc(day, 'practice part 1', part1_calc(lines), 11)
check_aoc(day, 'practice part 2', part2_calc(lines), 31)

lines = get_input(f'play/aoc-2024/{day:02}/real.txt')
check_aoc(day, 'for real part 1', part1_calc(lines), 1319616)
check_aoc(day, 'for real part 2', part2_calc(lines), 27267728)