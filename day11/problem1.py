#!/usr/bin/env python3

import sys
from collections import defaultdict
from itertools import chain
        
def get_input():
    return sys.stdin.read().splitlines()

def input_to_stones(lines):
    return [int(x) for x in lines[0].strip().split()]

def morph(stone):
    if stone == 0:
        return [1]
    str_val = str(stone)
    str_len = len(str_val)
    if str_len % 2 == 0:
        mid = str_len // 2
        return [int(str_val[:mid]), int(str_val[mid:])]
    return [stone * 2024]

def blink(stones):
    for stone in stones:
        yield from morph(stone)

if __name__ == "__main__":
    line = input_to_stones(get_input())
    for _ in range(25):
        line = blink(line)
    print(len(list(line)))
