#!/usr/bin/env python3

import sys

def get_input():
    return sys.stdin.read()

def parse_input(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    tokens = [t.strip() for t in lines[0].split(',')]
    sequences = lines[1:]
    return tokens, sequences

def is_makeable(value, towels, makeable, not_makeable):
    if value in makeable:
        return True

    if value in not_makeable:
        return False
    
    print('checking:', value)
    for sequence in towels:
        if value.startswith(sequence):
            shortened_value = value[len(sequence):]
            if is_makeable(shortened_value, towels, makeable, not_makeable):
                makeable.add(value)
                return True
    not_makeable.add(value)
    return False

if __name__ == "__main__":
    towels, sequences = parse_input(get_input())
    count = 0
    checked = 0
    makeable = set(towels)
    not_makeable = set()
    for sequence in sequences:
        if is_makeable(sequence, towels, makeable, not_makeable):
            count += 1
        checked += 1
    print('checked:', checked, 'count:', count)
    print(count)