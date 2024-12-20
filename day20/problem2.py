#!/usr/bin/env python3

import sys


right = 0+1j
left = 0-1j
down = 1+0j
up = -1+0j
all_directions = [right, left, down, up]

def get_input():
    return sys.stdin.read()

def parse_board(input):
    result = {}
    start = None
    end = None
    row = 0
    for line in input.strip().split("\n"):
        col = 0
        for char in line:
            coord = complex(row, col)
            if char == ".":
                result[coord] = 99999999
            elif char == "S":
                result[coord] = 99999999
                start = coord
            elif char == "E":
                result[coord] = 0
                end = coord
            else:
                result[coord] = None
            col += 1
        row += 1
    return result, start, end

def determine_distance_to_finish(map, start):
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

def determine_path(map, start, end):
    path = [start]
    current = start
    while current != end:
        for direction in all_directions:
            new_location = current + direction
            if new_location in map and map[new_location] == map[current] - 1:
                path.append(new_location)
                current = new_location
                break
    return path

def manhattan_distance(a, b):
    return int(abs(a.real - b.real) + abs(a.imag - b.imag))

def discover_shortcuts(map, path, threshold):
    shortcuts = set()
    for i in range(0, len(path) - 1):
        debug = path[i] == complex(47,25)
        for x in range(-20, 21):
            for y in range(-20, 21):
                endpoint = complex(x,y) + path[i]
                replacement_steps = manhattan_distance(path[i], endpoint)
                if replacement_steps <= 20 and endpoint in map and map[endpoint] is not None:
                    delta = map[path[i]] - map[endpoint]
                    total_savings = delta - replacement_steps
                    if total_savings >= threshold:
                        shortcuts.add((path[i], endpoint))
        
    return shortcuts

if __name__ == "__main__":
    map, start, end = parse_board(get_input())
    threshold = int(sys.argv[1])
    determine_distance_to_finish(map, end)
    path = determine_path(map, start, end)
    shortcuts = discover_shortcuts(map, path, threshold)
    print(len(shortcuts))