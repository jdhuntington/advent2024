#!/usr/bin/env python3

from problem1 import rotate_315, rotate_45
from math import floor

def find_middles(needle, haystack, positive_rotation):
    other_needle = needle[::-1]
    middles = []
    for i in range(len(haystack)):
        line = haystack[i]
        for pos in range(len(line)):
            if line.startswith(needle, pos) or line.startswith(other_needle, pos):
                middle = pos + floor(len(needle) / 2)
                if positive_rotation:
                    middles.append((i - middle, middle))
                else:
                    middles.append((i - (len(line) - middle) + 1, middle))
    return middles

if __name__ == "__main__":
    import fileinput

    lines = []
    for line in fileinput.input():
        lines.append(line.strip())


    middles_positive = find_middles('MAS', rotate_45(lines), True)
    middles_negative = find_middles('MAS', rotate_315(lines), False)

    print(len(set(middles_positive).intersection(set(middles_negative))))

