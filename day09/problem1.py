#!/usr/bin/env python3

import sys
from collections import defaultdict
from itertools import permutations
        
def get_input():
    return sys.stdin.read().splitlines()

def input_to_fs(content):
    i = 0
    result = []
    is_file = True
    for char in content.strip():
        length = int(char)
        if is_file:
            result.extend([i] * length)
            is_file = False
            i += 1
        else:
            result.extend([None] * length)
            is_file = True
    return result

def is_packed(fs):
    seen_none = False
    for x in fs:
        if x is None:
            seen_none = True
        elif seen_none:
            return False
    return True

def repack_fs(fs):
    print("fs length = ", len(fs))
    iteration = 0
    while not is_packed(fs):
        if iteration % 2000 == 0:
            print("iteration", iteration)
        first_none_index = next(i for i, x in enumerate(fs) if x is None)
        last_int_index = len(fs) - 1 - next(i for i, x in enumerate(reversed(fs)) if x is not None)
        fs[first_none_index] = fs[last_int_index]
        fs[last_int_index] = None
        iteration += 1

def checksum(fs):
    result = 0
    for i, id in enumerate(fs):
        if id:
            result += (i * id)
    return result

if __name__ == "__main__":
    fs = input_to_fs(get_input()[0])
    print('got fs')
    repack_fs(fs)
    print('repacked')
    print(checksum(fs))
