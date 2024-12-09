import sys
sys.path.append("play/aoc-2024/")
from common import *

###############################################################################
# CODING
###############################################################################
def parse(lines):
    page_rules = []
    update_pages = []

    for line in lines:
        if '|' in line:
            page_rules.append(line.split('|'))
        elif ',' in line:
            update_pages.append(line.split(','))

    return page_rules, update_pages

# PART1
def is_update_ok(page_rules, update):
    for rule in page_rules:
        try:
            if  update.index(rule[0]) > update.index(rule[1]):
                return False
        except: # no applicable rule found
            None
    return  True

def part1_calc(lines):
    running_total = 0
    page_rules, update_pages = parse(lines)
    for update in update_pages:
        if  is_update_ok(page_rules, update):
            running_total += int(update[int((len(update)-1)/2)])

    return  running_total

# PART2
def get_middle_element_of_correct_update(page_rules, update):
    for rule in page_rules[1:]:
        try:
            id0 = update.index(rule[0])
            id1 = update.index(rule[1])
            if  id0 > id1:
                update.insert(id1, update.pop(id0))
                # print("becomes: ", update, rule)
        except: # no applicable rule found
            None

    if  is_update_ok(page_rules, update):
        return int(update[int((len(update)-1)/2)])
    else: # recurse until all rules ok
        return get_middle_element_of_correct_update(page_rules, update)

def part2_calc(lines):
    running_total = 0
    page_rules, update_pages = parse(lines)
    for update in update_pages:
        if  not is_update_ok(page_rules, update):
            running_total += get_middle_element_of_correct_update(page_rules, update)
    return  running_total

###############################################################################
# Running
###############################################################################
day   = 5
tbd   = 0
lines = get_input(f'play/aoc-2024/{day:02}/practice.txt')
check_aoc(day, 'practice part 1', part1_calc(lines), 143)
check_aoc(day, 'practice part 2', part2_calc(lines), 123)

# ###############################################################################
lines = get_input(f'play/aoc-2024/{day:02}/real.txt')
check_aoc(day, 'for real part 1', part1_calc(lines), 5108)
check_aoc(day, 'for real part 2', part2_calc(lines), 7380)
