#!/usr/bin/env python3

import sys
from collections import defaultdict

directions = {
    'right': 0+1j,
    'left': 0-1j,
    'down': 1+0j,
    'up': -1+0j
}

def get_input():
    return sys.stdin.read().splitlines()


def input_to_map(lines):
    result = {}
    for i, line in enumerate(lines):
        for j, x in enumerate(line.strip()):
            pos = complex(i, j)
            result[pos] = x
    return result

def make_region(map, visited, working_region, current_position, expected_char):
    if not current_position in map:
        return

    if map[current_position] != expected_char:
        return

    if current_position in visited:
        return

    visited.add(current_position)
    working_region.append(current_position)

    make_region(map, visited, working_region, current_position + directions['right'], expected_char)
    make_region(map, visited, working_region, current_position + directions['left'], expected_char)
    make_region(map, visited, working_region, current_position + directions['up'], expected_char)
    make_region(map, visited, working_region, current_position + directions['down'], expected_char)
    
def make_regions(map):
    visited = set()
    result = []
    for pos in map:
        if not pos in visited:
            coords = []
            make_region(map, visited, coords, pos, map[pos])
            result.append((map[pos], coords))
    return result

def discover_fence_cost(region):
    character, coordinates = region
    spans = defaultdict(int)
    # 0 horizontal
    # 1 vertical
    vertices = set()
    for location in coordinates:
        spans[(location, location + directions['right'], 0)] += 1
        spans[(location, location + directions['down'], 1)] += 1
        spans[(location + directions['right'], location + directions['down'] + directions['right'], 1)] += 1
        spans[(location + directions['down'], location + directions['down'] + directions['right'], 0)] += 1

        vertices.add(location)
        vertices.add(location + directions['down'])
        vertices.add(location + directions['right'])
        vertices.add(location + directions['down'] + directions['right'])


    segments = []
    for span, count in spans.items():
        if count == 1:
            segments.append(span)
        else:
            v0, v1, _ = span
            if v0 in vertices:
                vertices.remove(v0)
            if v1 in vertices:
                vertices.remove(v1)
    
    print(vertices)
            
    updated = True
    while updated:
        updated = False
        i = 0
        while i < len(segments):
            segment0 = segments[i]
            v00, v01, orientation0 = segment0

            j = i + 1
            while j < len(segments):
                segment1 = segments[j]
                v10, v11, orientation1 = segment1
                
                if orientation0 != orientation1:
                    j += 1
                    continue
                
                new_segment = None
                if v00 == v10 and (not v00 in vertices):
                    new_segment = (v01, v11, orientation0)
                elif v01 == v10 and (not v01 in vertices):
                    new_segment = (v00, v11, orientation0)
                elif v00 == v11 and (not v00 in vertices):
                    new_segment = (v01, v10, orientation0)
                elif v01 == v11 and  (not v01 in vertices):
                    new_segment = (v00, v10, orientation0)
                
                if new_segment:
                    updated = True
                    segments.pop(j)
                    segments.pop(i)
                    segments.append(new_segment)
                    break
                
                j += 1
            
            if updated:
                break
            
            i += 1
    print(segments)
    return len(segments) * len(coordinates)
            
if __name__ == "__main__":
    map = input_to_map(get_input())
    regions = make_regions(map)
    fences = [discover_fence_cost(region) for region in regions]
    print(sum(fences))
