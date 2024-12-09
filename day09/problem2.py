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

def rehome_blocks(fs, start, end, rehomed_ids):
    if fs[start] in rehomed_ids:
        return
    rehomed_ids.add(fs[start])
    if fs[start] == 5437 or fs[start] == 5433:
        print("Trying to rehome", start, end, fs[start:end+1])
    current_empty_block_start = -1
    on_empty_block = False
    for i in range(start):
        if fs[i] is None:
            if on_empty_block:
                current_empty_blocks = i - current_empty_block_start
                if current_empty_blocks >= (end - start):
                    if fs[start] == 5437 or fs[start] == 5433:
                        print("Rehoming to", current_empty_block_start, "-", i)
                    fs[current_empty_block_start:(i+1)] = fs[start:end+1]
                    fs[start:end+1] = [None] * (end - start + 1)
                    return
            elif start == end:
                fs[i:(i+1)] = fs[start:end+1]
                fs[start:end+1] = [None] * (end - start + 1)
            else:
                on_empty_block = True
                current_empty_block_start = i
        else:
            current_empty_block_start = -1
            on_empty_block = False

def repack_fs(fs):
    current_element = None
    current_element_start = -1
    current_element_end = -1
    rehomed = set()
    # Transitions
    # DONE None -> blocka: start recording
    # DONE blocka -> blockb: move blockb, start recording
    # DONE blockb -> None: move blockbx
    # DONE blocka -> blocka: move start pointer
    # None -> None: Do nothing
    for i in range(len(fs)-1, -1, -1):
        #        print(fs)
        active = fs[i]
        if current_element is None and active is not None:
            current_element = fs[i]
            current_element_start = i
            current_element_end = i
        elif current_element == active:
            current_element_start = i
        elif current_element is not None and active is None:
            rehome_blocks(fs, current_element_start, current_element_end, rehomed)
            current_element = None
            current_element_start = -1
            current_element_end = -1
        elif current_element is None and active is None:
            current_element = None
            current_element_start = -1
            current_element_end = -1
        elif current_element != active:
            # print('current_element changed', current_element, active)
            rehome_blocks(fs, current_element_start, current_element_end, rehomed)
            current_element = active
            current_element_start = i
            current_element_end = i
        else:
            raise ValueError("Unexpected condition", active, "current", current_element, current_element_start, current_element_end)
def checksum(fs):
    result = 0
    for i, id in enumerate(fs):
        if id:
            result += (i * id)
    return result

if __name__ == "__main__":
    fs = input_to_fs(get_input()[0])
    repack_fs(fs)

    # for val in fs:
    #     print(val)
    print(checksum(fs))
