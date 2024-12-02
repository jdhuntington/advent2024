#!/usr/bin/env python3

def line_to_ints(str):
    return [int(s) for s in str.split()]

def ascending(lst):
    return all(x < y for x, y in zip(lst, lst[1:]))

def descending(lst):
    return all(x > y for x, y in zip(lst, lst[1:]))

def intervals_ok(lst):
    return all((1 <= abs(x - y) <= 3) for x, y in zip(lst, lst[1:]))

def try_removing_each(lst):
    for i in range(len(lst)):
        sublist = lst[:i] + lst[i+1:]
        yield sublist

if __name__ == "__main__":
    import fileinput
    from itertools import permutations

    sum = 0

    for line in fileinput.input():
        measures = line_to_ints(line)
        for sublist in try_removing_each(measures):
            if ((ascending(sublist) or descending(sublist)) and intervals_ok(sublist)):
                sum +=1
                break

    print(sum)
