#!/usr/bin/env python3

def sorted_int_list(input):
    result = [int(s) for s in input]
    return sorted(result)

def check_ocurrecurrences(l1, l2):
    result = 0
    for el in l1:
        hits = 0
        for el2 in l2:
            if el == el2:
                hits += 1
        result += hits * el
    return result


if __name__ == "__main__":
    import fileinput

    pairs = []
    for line in fileinput.input():
        pairs.append(line.split())

    col1, col2 = zip(*pairs)

    answer = check_ocurrecurrences(sorted_int_list(col1), sorted_int_list(col2))

    print(answer)
