#!/usr/bin/env python3

import sys
from functools import cache

def get_input():
    return sys.stdin.read()

def parse_input(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    tokens = [t.strip() for t in lines[0].split(',')]
    sequences = lines[1:]
    return tuple(tokens), sequences

@cache
def solution_count(value, towels):
    if value == '':
        return 1

    count = 0
    for towel in towels:
        if value.startswith(towel):
            count += solution_count(value.removeprefix(towel), towels)
    return count

if __name__ == "__main__":
    towels, sequences = parse_input(get_input())
    count = 0
    for sequence in sequences:
        result = solution_count(sequence, towels)
        count += result
    print('total', count)