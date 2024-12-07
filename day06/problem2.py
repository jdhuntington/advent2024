#!/usr/bin/env python3

def parse_input():
    lines = list(iter(input, ''))
    height = len(lines)
    width = len(lines[0])
    
    board = [[None] * width for y in range(height)]
    direction = (0,0)
    location = (-1,-1)
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                board[y][x] = True
            if char == '^':
                location = (x,y)
                direction = (0, -1)
    
    return board, location, direction

def location_valid(board, location):
    x,y = location
    w = len(board[0])
    h = len(board)
    return 0 <= x < w and 0 <= y < h

def add_tuple(t1, t2):
    x1, y1 = t1
    x2, y2 = t2
    return (x1+x2, y1+y2)

def turn_right(direction):
    if direction == (1,0):
        return (0,1)
    if direction == (0,1):
        return (-1, 0)
    if direction == (-1,0):
        return (0, -1)
    if direction == (0,-1):
        return (1,0)

def step(board, location, direction):
    if not location_valid(board, add_tuple(location, direction)):
        return add_tuple(location, direction), direction
    while True:
        next_location = add_tuple(location, direction)
        nx, ny = next_location
        if not board[ny][nx]:
            return next_location, direction
        direction = turn_right(direction)

def halts(board, location, direction):
    seen = set()
    while location_valid(board, location):
        seen.add((location, direction))
        location, direction = step(board, location, direction)
        if (location, direction) in seen:
            return False
    return True

if __name__ == "__main__":
    board, location, direction = parse_input()
    option_count = 0

    visited = set()
    original_location = location
    original_direction = direction

    while location_valid(board, original_location):
        visited.add(original_location)
        original_location, original_direction = step(board, original_location, original_direction)

    for x,y in visited:
        if not (x,y) == location and not board[y][x]:
            board[y][x] = True
            if not halts(board, location, direction):
                option_count += 1
            board[y][x] = None
    print(option_count)
