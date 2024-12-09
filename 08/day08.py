import sys
proj_path = '/mnt/c/Users/Public/work/play/aoc-2024/'
sys.path.append(proj_path)
from common import *

###############################################################################
# CODING
###############################################################################
def show(lines):
    for line in lines:
        print(line)
    print()

def gather_freqs(lines):
    symbol_set = set(''.join(lines))
    symbol_set.remove('.')
    return symbol_set

def update(lines, xx, yy, cc): # Update grid char: lines[xx][yy] = cc
    if xx >= 0 and yy >= 0 and xx < len(lines) and yy < len(lines):
        print(xx, yy)
        line      = list(lines[xx])
        line[yy]  = cc
        lines[xx] = ''.join(line)
        # show(lines)

# PART1
def part1_calc(lines):
    running_total = 0
    antinodes_map = copy.deepcopy(lines)
    freqs = gather_freqs(lines)
    scratchpad = {}
    for freq in freqs:
        scratchpad[freq] = []
        for xx, line in enumerate(lines):
            for yy, ch in enumerate(line):
                if  ch == freq:
                    scratchpad[freq].append([xx, yy])
        for perm in itertools.combinations(scratchpad[freq], 2):
            pt0 = perm[0]
            pt1 = perm[1]
            x_dist = (pt1[0] - pt0[0])
            y_dist = (pt1[1] - pt0[1])
            # print(perm, pt0[0] - x_dist, pt0[1] - y_dist, freq)
            update(antinodes_map, pt0[0] - x_dist, pt0[1] - y_dist, '#')
            update(antinodes_map, pt1[0] + x_dist, pt1[1] + y_dist, '#')

    for line in antinodes_map:
        for ch in line:
            if ch == '#':
                running_total += 1

    return  running_total

# PART2

def part2_calc(lines):
    running_total = 0
    antinodes_map = copy.deepcopy(lines)
    freqs = gather_freqs(lines)
    scratchpad = {}
    for freq in freqs:
        scratchpad[freq] = []
        for xx, line in enumerate(lines):
            for yy, ch in enumerate(line):
                if  ch == freq:
                    scratchpad[freq].append([xx, yy])
        for perm in itertools.combinations(scratchpad[freq], 2):
            pt0 = perm[0]
            pt1 = perm[1]
            x_dist = (pt1[0] - pt0[0])
            y_dist = (pt1[1] - pt0[1])
            # print(perm, pt0[0] - x_dist, pt0[1] - y_dist, freq)
            for ii in range(1, len(lines)-1):
                update(antinodes_map, pt0[0] - ii*x_dist, pt0[1] - ii*y_dist, '#')
                update(antinodes_map, pt1[0] + ii*x_dist, pt1[1] + ii*y_dist, '#')

    for line in antinodes_map:
        for ch in line:
            if ch != '.':
                running_total += 1

    return  running_total

###############################################################################
# Running
###############################################################################
day   = 8
tbd   = 0
lines = get_input(f'{proj_path}/{day:02}/practice.txt')
show(lines)
check_aoc(day, 'practice part 1', part1_calc(lines), 14)
check_aoc(day, 'practice part 2', part2_calc(lines), 34)

# # ###############################################################################
lines = get_input(f'{proj_path}/{day:02}/real.txt')
check_aoc(day, 'for real part 1', part1_calc(lines), 254)
check_aoc(day, 'for real part 2', part2_calc(lines), 951)
