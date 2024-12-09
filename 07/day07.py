import sys
proj_path = '/mnt/c/Users/Public/work/play/aoc-2024/'
sys.path.append(proj_path)
from common import *

###############################################################################
# CODING
###############################################################################
# PART1
def check_equality(exp, acc, ops_list):
    if  len(ops_list) == 0:
        return exp == acc
    else:
        return check_equality(exp, acc + int(ops_list[0]), ops_list[1:]) \
            or check_equality(exp, acc * int(ops_list[0]), ops_list[1:])

def part1_calc(lines):
    running_total = 0
    for equation in lines:
        val, ops = equation.split(':')
        val = int(val)
        ops_list = ops.split()
        if check_equality(val, int(ops_list[0]), ops_list[1:]):
            running_total += val
    return  running_total

# PART2
def check_equality2(exp, acc, ops_list):
    if  len(ops_list) == 0:
        return exp == acc
    else:
        return check_equality2(exp, acc + int(ops_list[0]), ops_list[1:]) \
            or check_equality2(exp, acc * int(ops_list[0]), ops_list[1:]) \
            or check_equality2(exp, int(str(acc) + ops_list[0]), ops_list[1:])

def part2_calc(lines):
    running_total = 0
    for equation in lines:
        val, ops = equation.split(':')
        val = int(val)
        ops_list = ops.split()
        if check_equality2(val, int(ops_list[0]), ops_list[1:]):
            running_total += val
    return  running_total

###############################################################################
# Running
###############################################################################
day   = 7
tbd   = 0
lines = get_input(f'{proj_path}/{day:02}/practice.txt')
check_aoc(day, 'practice part 1', part1_calc(lines), 3749)
check_aoc(day, 'practice part 2', part2_calc(lines), 11387)

# # ###############################################################################
lines = get_input(f'{proj_path}/{day:02}/real.txt')
check_aoc(day, 'for real part 1', part1_calc(lines), 1298300076754)
check_aoc(day, 'for real part 2', part2_calc(lines), 248427118972289)
