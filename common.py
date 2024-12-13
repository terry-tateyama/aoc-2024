import copy
import re
import sys
sys.setrecursionlimit(15000)
import itertools
from   collections import defaultdict

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
