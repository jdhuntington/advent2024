#!/usr/bin/env python3

import sys
from collections import defaultdict
from itertools import permutations

def add_tuple(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def distance(t1, t2):
    return (t2[0] - t1[0], t2[1] - t1[1])

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.antennas = defaultdict(list)

    def __repr__(self):
        return f"Map(width={self.width}, height={self.height}, antennas={dict(self.antennas)})"

    def add_antenna(self, label, x, y):
        self.antennas[label].append((x,y))

    def populate(self, lines):
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if not char == '.':
                    self.add_antenna(char, x, y)

    def antinodes(self):
        result = set()
        for list in self.antennas.values():
            for item1, item2 in permutations(list, 2):
                dxdy = distance(item1, item2)
                antinode_location = add_tuple(item2, dxdy)
                if self.in_bounds(antinode_location):
                    result.add(antinode_location)
        return result

    def in_bounds(self, coords):
        x,y = coords
        return 0 <= x < self.width and 0 <= y < self.height
                    
        
def get_input():
    return sys.stdin.read().splitlines()

if __name__ == "__main__":
    content = get_input()
    map = Map(len(content[0]), len(content))
    map.populate(content)
    print(map)
    antinodes = map.antinodes()
    print(antinodes)
    print(len(antinodes))
