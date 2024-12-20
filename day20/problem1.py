#!/usr/bin/env python3

import sys


right = 0+1j
left = 0-1j
down = 1+0j
up = -1+0j
all_directions = [right, left, down, up]
double_moves = [right + right, left + left, down + down, up + up]

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
    path = []
    current = start
    while current != end:
        for direction in all_directions:
            new_location = current + direction
            if new_location in map and map[new_location] == map[current] - 1:
                path.append(new_location)
                current = new_location
                break
    return path

def discover_shortcuts(map, path, threshold):
    shortcuts = []
    for i in range(0, len(path) - 1):
        for direction in double_moves:
            new_location = path[i] + direction
            if new_location in path and ((map[path[i]] - map[new_location] - 2) >= threshold):
                shortcuts.append((path[i], new_location, map[path[i]] - map[new_location] - 2))
    return shortcuts

if __name__ == "__main__":
    map, start, end = parse_board(get_input())
    threshold = int(sys.argv[1])
    determine_distance_to_finish(map, end)
    path = determine_path(map, start, end)
    shortcuts = discover_shortcuts(map, path, threshold)
    print(shortcuts)
    print(len(shortcuts))