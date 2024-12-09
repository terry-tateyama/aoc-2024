import sys
sys.path.append("play/aoc-2024/")
from common import *

###############################################################################
# CODE
###############################################################################

# PART1
def part1_calc(lines):
    running_total = 0
    for line in lines:
        re_captures = re.findall(r'mul\((\d+),(\d+)\)', line) # [('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]
        for cap1, cap2 in re_captures:
            running_total += int(cap1) * int(cap2) # 2 * 4  + ...
    return running_total

# PART2
def part2_calc(lines):
    running_total = 0
    enabled = True
    for line in lines:
        re_captures = re.findall(r"(don't\(\)|do\(\)|mul\((\d+),(\d+)\))", line)
        for cmd, cap1, cap2 in re_captures:
            # print(cmd, cap1, cap2)
            match cmd:
                case "do()"     : enabled = True
                case "don't()"  : enabled = False
                case _: # else "mul(...)"
                    if enabled: 
                        running_total += int(cap1) * int(cap2)
    return running_total

###############################################################################
# RUNNING
###############################################################################
day   = 3
lines = get_input(f'play/aoc-2024/{day:02}/practice.txt')
check_aoc(day, 'practice part 1', part1_calc(lines), 161)
check_aoc(day, 'practice part 2', part2_calc(lines), 48)

lines = get_input(f'play/aoc-2024/{day:02}/real.txt')
check_aoc(day, 'for real part 1', part1_calc(lines), 157621318)
check_aoc(day, 'for real part 2', part2_calc(lines), 79845780)