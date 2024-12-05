#!/usr/bin/env python3

from graphlib import TopologicalSorter

def build_global_ordering(pairs):
    graph = {}
    for before, after in pairs:
        if after not in graph:
            graph[after] = set()
        if before not in graph:
            graph[before] = set()
        graph[after].add(before)
    return list(TopologicalSorter(graph).static_order())

def middle_number(seq):
    return seq[len(seq) // 2]
    
def valid_ordering(constraint_pairs, test):
    constraints = build_global_ordering(constraint_pairs)
    last_pos = -1
    for element in test:
        next_pos = constraints.index(element)
        if next_pos <= last_pos:
            return False
        last_pos = next_pos
    return True

if __name__ == "__main__":
    import fileinput

    rules = []
    updates = []

    seen_newline = False

    for line in fileinput.input():
        if not seen_newline:
            val = line.strip()
            if len(val) == 0:
                seen_newline = True
            else:
                rules.append(val)
        else:
            updates.append(line.strip())

    rule_pairs = [tuple(map(int, s.split("|"))) for s in rules]
    total = 0
    for s in updates:
        vals = [int(x) for x in s.split(",")]
        applicable_pairs = [(a,b) for a,b in rule_pairs if a in vals and b in vals]
        if valid_ordering(applicable_pairs, vals):
            total += middle_number(vals)

    print(total)
