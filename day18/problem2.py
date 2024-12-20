#!/usr/bin/env python3

import sys


right = 0+1j
left = 0-1j
down = 1+0j
up = -1+0j
all_directions = [right, left, down, up]

def get_input():
    return sys.stdin.read()

def parse_memory_locations(input):
    result = []
    for line in input.strip().split("\n"):
        x,y = line.split(",")
        result.append(complex(int(x), int(y)))
    return result

def find_shortest_walk(map, start):
    locations_to_check = set()
    locations_to_check.add(start)
    while len(locations_to_check) > 0:
        current = locations_to_check.pop()
        value = map[current]
        for direction in all_directions:
            new_location = current + direction
            if new_location in map and map[new_location] is not None and (map[new_location] > value + 1):
                map[new_location] = value + 1
                locations_to_check.add(new_location)

if __name__ == "__main__":
    locations = parse_memory_locations(get_input())
    dimensions = int(sys.argv[1])
    map = {}
    for i in range(dimensions):
        for j in range(dimensions):
            map[complex(i,j)] = 99999999

    map[complex(dimensions-1, dimensions-1)] = 0
    for bytes_to_drop in range(len(locations)):
        # Clone map
        new_map = map.copy()
        for i in range(bytes_to_drop):
            new_map[locations[i]] = None
        find_shortest_walk(new_map, complex(dimensions-1, dimensions-1))
        print(bytes_to_drop, new_map[complex(0,0)], locations[bytes_to_drop - 1])