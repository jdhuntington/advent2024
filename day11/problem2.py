#!/usr/bin/env python3

import sys
from collections import defaultdict

def get_input():
    return sys.stdin.read().splitlines()

def input_to_stones(lines):
    result = defaultdict(int)
    for x in lines[0].strip().split():
        result[int(x)] += 1
    return result

def count_digits(n):
    if n == 0:
        return 1
    count = 0
    while n:
        count += 1
        n //= 10
    return count

def split_number(n, digit_count):
    divisor = 10 ** (digit_count // 2)
    return n // divisor, n % divisor

def morph(stone):
    if stone == 0:
        return [1]
    
    digit_count = count_digits(stone)
    if digit_count % 2 == 0:
        first, second = split_number(stone, digit_count)
        return [first, second]
    return [stone * 2024]

class LazyDict(dict):
    def __init__(self, factory):
        super().__init__()
        self.factory = factory

    def __missing__(self, key):
        value = self.factory(key)
        self[key] = value
        return value

def blink(line, lookup):
    result = defaultdict(int)
    for k, v in line.items():
        for new_stone in lookup[k]:
            result[new_stone] += v
    return result
    

if __name__ == "__main__":
    line = input_to_stones(get_input())
    lookup = LazyDict(morph)
    for x in range(75):
        line = blink(line, lookup)
        print(x, sum(line.values()))
