import sys
proj_path = '/mnt/c/Users/Public/work/play/aoc-2024/'
sys.path.append(proj_path)
from common import *

summits_reached = []
###############################################################################
# CODING
###############################################################################
# Display puzzle grid (map of heights)
def show(lines):
    if  len(lines) == 8: # practice
        print('\n  01234567')
    for xx, line in enumerate(lines):
        print(xx, line)
    print()

# If xx, yy is within the grid, return height[xx][yy]
# else INVALID (-1)
def lookup(lines, xx, yy):
    max_dim = len(lines)
    result  = -1 # INVALID
    if xx >= 0 and xx < max_dim and yy >= 0 and yy < max_dim:
           result = lines[xx][yy]
    return result

# Is a neighbor block (at xx, yy) a step higher than prev_height?
def is_a_step_up_(lines, xx, yy, prev_height): 
    return  int(int(lookup(lines, xx, yy)) == prev_height + 1)

def score(lines, xx, yy, is_part1=True):
    height = int(lookup(lines, xx, yy))
    if  height < 0 or height > 9: return 0 # fallen off the map

    result = 0
    if  height == 8: # recursion termination condition
        result += is_new_summit_reached(lines, xx-1, yy, height, is_part1) # N
        result += is_new_summit_reached(lines, xx+1, yy, height, is_part1) # S
        result += is_new_summit_reached(lines, xx, yy-1, height, is_part1) # W
        result += is_new_summit_reached(lines, xx, yy+1, height, is_part1) # E
    else: # recurse to score each higher adjacent step
        result += score__ascending_step(lines, xx-1, yy, height, is_part1) # N
        result += score__ascending_step(lines, xx+1, yy, height, is_part1) # S
        result += score__ascending_step(lines, xx, yy-1, height, is_part1) # W
        result += score__ascending_step(lines, xx, yy+1, height, is_part1) # E
    return result

def score__ascending_step(lines, xx, yy, height, is_part1):
    if  not is_a_step_up_(lines, xx, yy, height):
        return 0 # terminate recursion if not ascending
    return score(lines, xx, yy, is_part1) # keep ascending at new(xx, yy)

# Keep track of (xx, yy) for summits previously reached
def reached_summit(xx, yy):
    try:
        summits_reached.index([xx, yy])
        return True
    except:
        summits_reached.append([xx, yy])
        return False

def is_new_summit_reached(lines, xx, yy, prev_height, is_part1):
    if  not is_a_step_up_(lines, xx, yy, prev_height):  return 0
    if  not is_part1 or not reached_summit(xx, yy):     return 1
    return 0

def get_list_of_trailhead_scores(lines, is_part1=True, trailhead_symbol='0'):
    scores = []
    for xx, line in enumerate(lines):
        for yy, height in enumerate(line):
            if  lines[xx][yy] == trailhead_symbol:
                global summits_reached
                summits_reached = [] # reset for each new potential trailhead
                scores.append(score(lines, xx, yy, is_part1))
                # print(lines[xx][yy], ':', xx, yy, scores)
    return scores

# PART1
def part1_calc(lines):
    scores = get_list_of_trailhead_scores(lines)
    return sum(scores)

# PART2
def part2_calc(lines):
    scores = get_list_of_trailhead_scores(lines, is_part1=False)
    return sum(scores)

###############################################################################
# Running
###############################################################################
day   = 10
tbd   = 0
lines = get_input(f'{proj_path}/{day:02}/practice.txt')
check_aoc(day, 'practice part 1', part1_calc(lines), 36)
check_aoc(day, 'practice part 2', part2_calc(lines), 81)

###############################################################################
lines = get_input(f'{proj_path}/{day:02}/real.txt')
check_aoc(day, 'for real part 1', part1_calc(lines), 548)
check_aoc(day, 'for real part 2', part2_calc(lines), 1252)