import sys
proj_path = '/mnt/c/Users/Public/work/play/aoc-2024/'
sys.path.append(proj_path)
from common import *

###############################################################################
# GLOBALS (YUCK)
###############################################################################
summits_reached = []

###############################################################################
# CODING
###############################################################################
def show(lines):
    if  len(lines) == 8: # practice
        print('\n  01234567')
    for xx, line in enumerate(lines):
        print(xx, line)
    print()

def lookup(lines, xx, yy):
    max_dim = len(lines)
    result  = -1 # invalid
    if xx >= 0 and xx < max_dim and yy >= 0 and yy < max_dim:
           result = lines[xx][yy]
    return result

def is_step_up(lines, xx, yy, prev_height):
    return  int(int(lookup(lines, xx, yy)) == prev_height + 1)

def reached_summit(xx, yy):
    global  summits_reached
    try:
            summits_reached.index([xx, yy])
            return True
    except:
            summits_reached.append([xx, yy])
            return False

def score(lines, xx, yy):
    height = int(lookup(lines, xx, yy))
    if  height < 0 or height > 9:
        return 0

    result = 0
    if  height == 8: # recursion termination condition
        result += int(is_step_up(lines, xx-1, yy, height) and not reached_summit(xx-1, yy))
        result += int(is_step_up(lines, xx+1, yy, height) and not reached_summit(xx+1, yy))
        result += int(is_step_up(lines, xx, yy-1, height) and not reached_summit(xx, yy-1))
        result += int(is_step_up(lines, xx, yy+1, height) and not reached_summit(xx, yy+1))
    else:
        if  is_step_up(lines, xx-1, yy, height): result += score(lines, xx-1, yy)
        if  is_step_up(lines, xx+1, yy, height): result += score(lines, xx+1, yy)
        if  is_step_up(lines, xx, yy-1, height): result += score(lines, xx, yy-1)
        if  is_step_up(lines, xx, yy+1, height): result += score(lines, xx, yy+1)
    return  result

# PART1
def part1_calc(lines):
    global summits_reached
    scores = []
    for xx, line in enumerate(lines):
        for yy, height in enumerate(line):
            summits_reached = []
            if  lines[xx][yy] == '0':
                scores.append(score(lines, xx, yy))
                # print(lines[xx][yy], ':', xx, yy, scores)
    # print(scores)
    return sum(scores)

# PART2
def score2(lines, xx, yy):
    height = int(lookup(lines, xx, yy))
    if  height < 0 or height > 9:
        return 0

    result = 0
    if  height == 8: # recursion termination condition
        result += int(is_step_up(lines, xx-1, yy, height))
        result += int(is_step_up(lines, xx+1, yy, height))
        result += int(is_step_up(lines, xx, yy-1, height))
        result += int(is_step_up(lines, xx, yy+1, height))
    else:
        if  is_step_up(lines, xx-1, yy, height): result += score2(lines, xx-1, yy)
        if  is_step_up(lines, xx+1, yy, height): result += score2(lines, xx+1, yy)
        if  is_step_up(lines, xx, yy-1, height): result += score2(lines, xx, yy-1)
        if  is_step_up(lines, xx, yy+1, height): result += score2(lines, xx, yy+1)
    return  result

def part2_calc(lines):
    scores = []
    for xx, line in enumerate(lines):
        for yy, height in enumerate(line):
            if  lines[xx][yy] == '0':
                scores.append(score2(lines, xx, yy))
                # print(lines[xx][yy], ':', xx, yy, scores)
    # print(scores)
    return sum(scores)
###############################################################################
# Running
###############################################################################
day   = 10
tbd   = 0
lines = get_input(f'{proj_path}/{day:02}/practice.txt')
show(lines)
check_aoc(day, 'practice part 1', part1_calc(lines), 36)
check_aoc(day, 'practice part 2', part2_calc(lines), 81)

# # ###############################################################################
lines = get_input(f'{proj_path}/{day:02}/real.txt')
check_aoc(day, 'for real part 1', part1_calc(lines), 548)
check_aoc(day, 'for real part 2', part2_calc(lines), 1252)