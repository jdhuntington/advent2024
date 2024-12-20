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
    pre_run = int(sys.argv[2])
    map = {}
    for i in range(dimensions):
        for j in range(dimensions):
            map[complex(i,j)] = 99999999

    for i in range(pre_run):
        map[locations[i]] = None

    for i in range(dimensions):
        for j in range(dimensions):
            coord = complex(i,j)
            if map[coord] is not None:
                # print '.' without newline
                print(".", end="")
            else:
                # print 'X' without newline
                print("X", end="")
        print()

    map[complex(dimensions-1, dimensions-1)] = 0
    find_shortest_walk(map, complex(dimensions-1, dimensions-1))
    print(map[complex(0,0)])