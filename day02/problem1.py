#!/usr/bin/env python3

def line_to_ints(str):
    return [int(s) for s in str.split()]

def ascending(lst):
    return all(x < y for x, y in zip(lst, lst[1:]))

def descending(lst):
    return all(x > y for x, y in zip(lst, lst[1:]))

def intervals_ok(lst):
    return all((1 <= abs(x - y) <= 3) for x, y in zip(lst, lst[1:]))


if __name__ == "__main__":
    import fileinput

    sum = 0

    for line in fileinput.input():
        measures = line_to_ints(line)
        if ((ascending(measures) or descending(measures)) and intervals_ok(measures)):
            sum +=1 

    print(sum)
