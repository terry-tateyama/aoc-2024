###############################################################################
# COMMON
###############################################################################
def get_input(filespec):
    with open(filespec) as file:
            lines = [line.rstrip() for line in file]
    return  lines

def check_aoc(day, doc_str, actual, expected):
    print(f'DAY{day:02} ({doc_str}):\t{actual}')
    assert(actual == expected)

###############################################################################
# CODING
###############################################################################
# For orientation with the input, 
#   X increments down   V
#   Y increments across ->
def lookup(lines, xid, yid, lmt):
    if xid < 0 or yid < 0 or xid >= lmt or yid >= lmt:
        return '.'
    else:
        return lines[xid][yid]

# PART1
def find_xmas(lines, xid, yid, xinc, yinc):
    lmt = len(lines) # needed since python allows negative indices
    xmas = 'X' \
         + lookup(lines, xid + 1*xinc, yid + 1*yinc, lmt) \
         + lookup(lines, xid + 2*xinc, yid + 2*yinc, lmt) \
         + lookup(lines, xid + 3*xinc, yid + 3*yinc, lmt)
    return int(xmas == 'XMAS')

def part1_calc(lines):
    running_total = 0
    for xid, line in enumerate(lines):
        for yid, letter in enumerate(line):
            if  letter == 'X':
                running_total += find_xmas(lines, xid, yid,  0,  1) # right
                running_total += find_xmas(lines, xid, yid,  0, -1) # left
                running_total += find_xmas(lines, xid, yid,  1,  0) # down
                running_total += find_xmas(lines, xid, yid, -1,  0) # up
                running_total += find_xmas(lines, xid, yid,  1,  1) # SE
                running_total += find_xmas(lines, xid, yid,  1, -1) # SW
                running_total += find_xmas(lines, xid, yid, -1,  1) # NE
                running_total += find_xmas(lines, xid, yid, -1, -1) # NW
    return      running_total

# PART2
def find_x_mas(lines, xid, yid):
    lmt = len(lines)
    ms1 = lookup(lines, xid - 1, yid - 1, lmt) + lookup(lines, xid + 1, yid + 1, lmt)
    ms2 = lookup(lines, xid + 1, yid - 1, lmt) + lookup(lines, xid - 1, yid + 1, lmt)
    return int(ms1 in ["MS", "SM"] and ms2 in ["MS", "SM"])

def part2_calc(lines):
    running_total = 0
    for xid, line in enumerate(lines):
        for yid, letter in enumerate(line):
            if  letter == 'A': # the middle of the X
                running_total += find_x_mas(lines, xid, yid)
    return running_total

###############################################################################
# Running
###############################################################################
day   = 4
lines = get_input(f'play/advent2024/{day:02}/practice.txt')
check_aoc(day, 'practice part 1', part1_calc(lines), 18)
check_aoc(day, 'practice part 2', part2_calc(lines), 9)

###############################################################################
lines = get_input(f'play/advent2024/{day:02}/real.txt')
check_aoc(day, 'for real part 1', part1_calc(lines), 2524)
check_aoc(day, 'for real part 2', part2_calc(lines), 1873)
