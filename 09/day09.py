import sys
proj_path = '/mnt/c/Users/Public/work/play/aoc-2024/'
sys.path.append(proj_path)
from common import *

###############################################################################
# CODING
###############################################################################
def show(blocks):
    result = ''.join(blocks)
    # print( result)
    return result 

def is_even(num):
    return num % 2 == 0

def parse(disk_map):
    blocks = []
    file_id = 0 # starting id
    for block_id, ch in enumerate(disk_map):
        if  is_even(block_id):
            for _ in range(int(ch)):
                blocks.append(str(file_id))
            file_id += 1
        else:
            for _ in range(int(ch)):
                blocks.append('.')
    return blocks

assert(show(parse('12345')) == '0..111....22222')

def pop_real_block(blocks):
    last_non_empty = blocks.pop()
    if  last_non_empty != '.':
        return last_non_empty
    else:
        return pop_real_block(blocks)

def defrag_block(blocks):
    file_id = pop_real_block(blocks)
    try:
        empty_id = blocks.index('.')
        blocks[empty_id] = file_id
        return True
    except:
        blocks.append(file_id)
        return False

# PART1
def part1_calc(lines):
    blocks = parse(lines[0])
    show(blocks)
    while defrag_block(blocks):
        None

    return score(blocks)

def score(blocks):
    running_total = 0
    for pos, ch in enumerate(blocks):
        if ch != '.':
            running_total += pos * int(ch)
    return  running_total

# PART2
def defrag_files(blocks):
    saved_file_id = None
    for bck_id, file_id in reversed(list(enumerate(blocks))):
        if  file_id != '.' and file_id != saved_file_id: 
            saved_file_id, file_len = compute_file_meta_data(blocks, bck_id, file_id)
            defrag_file(blocks, saved_file_id, bck_id, file_len)

def defrag_file(blocks, saved_file_id, bck_id, file_len):
    # Now we have to find a space large enough to move the file to:
    free_block_count = 0
    for fwd_id, ch in enumerate(blocks):
        if  blocks[fwd_id] == '.':
            free_block_count += 1
        else:
            free_block_count = 0
        if  free_block_count >= file_len and fwd_id < bck_id:
            for count in range(file_len):
                blocks[fwd_id - count] = saved_file_id
                blocks[bck_id - count] = '.'
            break

def compute_file_meta_data(blocks, bck_id, file_id):
    saved_file_id = file_id
    probe_block_id = bck_id - 1
    file_len = 1

    while blocks[probe_block_id] == saved_file_id:
        probe_block_id -= 1
        file_len += 1
    return saved_file_id,file_len

def part2_calc(lines):
    blocks = parse(lines[0])
    defrag_files(blocks)
    return score(blocks)

###############################################################################
# Running
###############################################################################
day   = 9
tbd   = 0
lines = get_input(f'{proj_path}/{day:02}/practice.txt')
check_aoc(day, 'practice part 1', part1_calc(lines), 1928)
check_aoc(day, 'practice part 2', part2_calc(lines), 2858)

# # ###############################################################################
lines = get_input(f'{proj_path}/{day:02}/real.txt')
check_aoc(day, 'for real part 1', part1_calc(lines), 6344673854800)
check_aoc(day, 'for real part 2', part2_calc(lines), 6360363199987)
