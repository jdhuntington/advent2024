#!/usr/bin/env python3

def sorted_int_list(input):
    result = [int(s) for s in input]
    return sorted(result)

def absolute_distance(tuple):
    a,b = tuple
    return abs(a - b)

def total_absolute_distance(pairs):
    result = 0
    for pair in pairs:
        result += absolute_distance(pair)
    return result

if __name__ == "__main__":
    import fileinput

    pairs = []
    for line in fileinput.input():
        pairs.append(line.split())

    col1, col2 = zip(*pairs)
    distance_tuples = zip(sorted_int_list(col1), sorted_int_list(col2))

    answer = total_absolute_distance(distance_tuples)
    print(answer)
