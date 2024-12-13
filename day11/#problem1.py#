#!/usr/bin/env python3

import sys
from collections import defaultdict

directions = {
    'right': 0+1j,
    'left': 0-1j,
    'down': 1+0j,
    'up': -1+0j
}

def get_input():
    return sys.stdin.read().splitlines()


def input_to_map(lines):
    result = {}
    for i, line in enumerate(lines):
        for j, x in enumerate(line.strip()):
            pos = complex(i, j)
            result[pos] = x
    return result

def make_region(map, visited, working_region, current_position, expected_char):
    if not current_position in map:
        return

    if map[current_position] != expected_char:
        return

    if current_position in visited:
        return

    visited.add(current_position)
    working_region.append(current_position)

    make_region(map, visited, working_region, current_position + directions['right'], expected_char)
    make_region(map, visited, working_region, current_position + directions['left'], expected_char)
    make_region(map, visited, working_region, current_position + directions['up'], expected_char)
    make_region(map, visited, working_region, current_position + directions['down'], expected_char)
    
def make_regions(map):
    visited = set()
    result = []
    for pos in map:
        if not pos in visited:
            coords = []
            make_region(map, visited, coords, pos, map[pos])
            result.append((map[pos], coords))
    return result

def discover_fence_cost(region):
    character, coordinates = region
    spans = defaultdict(int)
    for location in coordinates:
        spans[(location, location + directions['right'])] += 1
        spans[(location, location + directions['down'])] += 1
        spans[(location + directions['right'], location + directions['down'] + directions['right'])] += 1
        spans[(location + directions['down'], location + directions['down'] + directions['right'])] += 1
    perimeter = 0
    for span, count in spans.items():
        if count == 1:
            perimeter += 1
    return perimeter * len(coordinates)
            
if __name__ == "__main__":
    map = input_to_map(get_input())
    regions = make_regions(map)
    fences = [discover_fence_cost(region) for region in regions]
    print(sum(fences))
