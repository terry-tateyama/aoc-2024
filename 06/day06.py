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

def find_guard(lines, guard_dir):
    for xx, line in enumerate(lines):
        try:
            yy = line.index(guard_dir)
            return xx, yy
        except:
            None

def turn_right(guard_dir):
    if guard_dir == '^': return '>'
    if guard_dir == '>': return 'v'
    if guard_dir == 'v': return '<'
    if guard_dir == '<': return '^'

def next_move(xx, yy, guard_dir):
    next_x = xx
    next_y = yy
    if   guard_dir == '^':  next_x = xx - 1
    elif guard_dir == 'v':  next_x = xx + 1
    elif guard_dir == '<':  next_y = yy - 1
    elif guard_dir == '>':  next_y = yy + 1
    return next_x, next_y

def update(lines, xx, yy, cc): # Update grid char: lines[xx][yy] = cc
    line      = list(lines[xx])
    line[yy]  = cc
    lines[xx] = ''.join(line)

def move_guard(lines, xx, yy, guard_dir):
    next_x, next_y = next_move(xx, yy, guard_dir)

    if  next_x < 0 or next_x >= len(lines) \
    or  next_y < 0 or next_y >= len(lines):
        update(lines, xx, yy, guard_dir) # mark that guard has left the building
        return False, -1, -1, 'X'        # mark that guard has left the building
    
    next_grid = lines[next_x][next_y]
    if  next_grid == '#' or next_grid == 'O': # hit obstacle (turn right)
        guard_dir = turn_right(guard_dir)
        update(lines, xx, yy, guard_dir)
        return  True, xx, yy, guard_dir

    # part 2:
    next_grid = lines[next_x][next_y]
    if next_grid == guard_dir: # This doesn't catch the back and forth case
        return False, -1, -1, 'O' # Retracing path (part 2 terminal condition)

    update(lines,     xx,     yy, guard_dir)
    update(lines, next_x, next_y, guard_dir)

    return  True, next_x, next_y, guard_dir

# PART1
def part1_calc(lines):
    guard_dir    = '^' # assumed initial guard direction
    xx, yy       = find_guard(lines, guard_dir)
    last_move_ok = True

    while last_move_ok:
          last_move_ok, xx, yy, guard_dir = move_guard(lines, xx, yy, guard_dir)
    # show(lines)
    
    running_total = 0
    for line in lines:
        running_total += line.count('^')
        running_total += line.count('v')
        running_total += line.count('>')
        running_total += line.count('<')

    return  running_total

# PART2
def part2_calc(lines):
    running_total = 0
    guard_dir     = '^'
    xx, yy        = find_guard(lines, guard_dir)
    # visible       = False
    max_total     = 0

    for xid, line in enumerate(lines):
        for yid, char in enumerate(line):
            if char != '#':
                puzzle_scratchpad = copy.deepcopy(lines)
                guard_dir         = '^'
                xx, yy            = find_guard(lines, guard_dir)
                update(puzzle_scratchpad, xid, yid, 'O')
                total_moves       = 0
                last_move_ok      = True
                while last_move_ok:
                      last_move_ok, xx, yy, guard_dir = move_guard(puzzle_scratchpad, xx, yy, guard_dir)
                      total_moves += 1
                      if  total_moves > 8000:
                          running_total += 1
                          break
                    #   if  visible:
                    #       show(puzzle_scratchpad)

                if  guard_dir == 'O': # start of retracing path
                    running_total += 1
                    if  max_total < total_moves:
                        max_total = total_moves
                        print(xid, yid, total_moves, running_total)

    return  running_total

###############################################################################
# Running
###############################################################################
day   = 6
tbd   = 0
lines = get_input(f'{proj_path}/{day:02}/practice.txt')
puzzle_scratchpad = copy.deepcopy(lines)

check_aoc(day, 'practice part 1', part1_calc(lines), 41)
check_aoc(day, 'practice part 2', part2_calc(puzzle_scratchpad), 6)

# # ###############################################################################
lines = get_input(f'{proj_path}/{day:02}/real.txt')
puzzle_scratchpad = copy.deepcopy(lines)

check_aoc(day, 'for real part 1', part1_calc(lines), 5208)
# check_aoc(day, 'for real part 2', part2_calc(puzzle_scratchpad), 1899) # Too low
# check_aoc(day, 'for real part 2', part2_calc(puzzle_scratchpad), 16058) # Too high
check_aoc(day, 'for real part 2', part2_calc(puzzle_scratchpad), 1972)
