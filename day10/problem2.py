#!/usr/bin/env python3

import sys
from collections import defaultdict
from itertools import permutations
        
def get_input():
    return sys.stdin.read().splitlines()

def input_to_map(lines):
    return [[int(x) for x in line.strip()] for line in lines]

def routes(map, expected_elevation, i, j, found):
    if i < 0 or j < 0:
        return 0
    if i >= len(map) or j >= len(map[0]):
        return 0
    value = map[i][j]
    if value != expected_elevation:
        return 0
    elif value == 9:
        if (i,j) in found:
            return 0
        else:
            found.add((i,j))
            return 1
    else:
        total = routes(map, expected_elevation + 1, i - 1, j, found) + routes(map, expected_elevation + 1, i + 1, j, found) + routes(map, expected_elevation + 1, i, j - 1, found) + routes(map, expected_elevation + 1, i, j + 1, found)
        if expected_elevation == 0:
            print(i, j, total)
        return total

if __name__ == "__main__":
    map = input_to_map(get_input())
    total = sum(routes(map, 0, i, j, set()) for i in range(len(map)) for j in range(len(map[0])))
    print(total)
