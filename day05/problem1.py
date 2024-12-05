#!/usr/bin/env python3

from graphlib import TopologicalSorter

def build_global_ordering(pairs):
    graph = {}
    nodes = {x for pair in pairs for x in pair}
    graph = {node: set() for node in nodes}
    for before, after in pairs:
        graph[after].add(before)
    return list(TopologicalSorter(graph).static_order())

def middle_number(seq):
    return seq[len(seq) // 2]

def parse_input():
    rules = []
    updates = []
    
    for line in iter(input, ''):
        rules.append(line.strip())
    
    for line in iter(input, ''):
        updates.append([int(x) for x in line.strip().split(',')])
        
    return [tuple(map(int, s.split('|'))) for s in rules], updates

if __name__ == "__main__":
    rules, updates = parse_input()
    total = 0
    for vals in updates:
        if vals == build_global_ordering([(a,b) for a,b in rules if a in vals and b in vals]):
            total += middle_number(vals)

    print(total)
