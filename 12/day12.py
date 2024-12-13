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
    for xx, line in enumerate(lines):
        print(xx, line)
    print()

# If xx, yy is within the grid, return height[xx][yy]
# else INVALID (-1)
def lookup(lines, xx, yy):
    max_dim = len(lines)
    result  = -1 # INVALID
    if  xx >= 0 and xx < max_dim and yy >= 0 and yy < max_dim:
           result = lines[xx][yy]
    return result

def gather_tokens(lines):
    return set(''.join(lines))

def calc_score(lines, scores, xx, yy):
    num_same_neighbors = 0
    token    =  lookup(lines, xx, yy)
    if token == lookup(lines, xx - 1, yy): num_same_neighbors += 1
    if token == lookup(lines, xx + 1, yy): num_same_neighbors += 1
    if token == lookup(lines, xx, yy - 1): num_same_neighbors += 1
    if token == lookup(lines, xx, yy + 1): num_same_neighbors += 1
    # if same_neighbors == 0: scores[xx][yy] = 4
    # if same_neighbors == 1: scores[xx][yy] = 3
    # if same_neighbors == 2: scores[xx][yy] = 2
    # if same_neighbors == 3: scores[xx][yy] = 1
    # if same_neighbors == 4: scores[xx][yy] = 0
    scores[xx][yy] = 4 - num_same_neighbors

def price(scores, token):
    area = 0
    perimeter = 0
    for xx, line in enumerate(scores):
        for yy, fences in enumerate(line):
            if  token == lookup(lines, xx, yy):
                area += 1
                perimeter += fences
    print(token, area, '*', perimeter, '=', area * perimeter)
    return area * perimeter

# PART1
def part1_calc(lines):
    tokens = sorted(gather_tokens(lines))

    scores = [[0 for _ in range(len(lines))] for _ in range(len(lines))]
    scored = [[0 for _ in range(len(lines))] for _ in range(len(lines))] 

    for xx, line in enumerate(lines):
        for yy, ch in enumerate(line):
            calc_score(lines, scores, xx, yy)

    show(scores)
    running_total = 0
    for token in tokens:
           running_total += price(scores, token)
    return running_total

# PART2
def part2_calc(lines):
    return 1

###############################################################################
# Running
###############################################################################
day   = 12
tbd   = 0
lines = get_input(f'{proj_path}/{day:02}/practice.txt')
check_aoc(day, 'practice part 1', part1_calc(lines), 1930)
check_aoc(day, 'practice part 2', part2_calc(lines), tbd)

###############################################################################
lines = get_input(f'{proj_path}/{day:02}/real.txt')
check_aoc(day, 'for real part 1', part1_calc(lines), tbd)
check_aoc(day, 'for real part 2', part2_calc(lines), tbd)