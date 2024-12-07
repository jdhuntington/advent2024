#!/usr/bin/env python3

def mult(expected, total, terms):
    running_total = total * terms[0]
    if len(terms) == 1:
        return running_total == expected
    return mult(expected, running_total, terms[1:]) or add(expected, running_total, terms[1:])

def add(expected, total, terms):
    running_total = total + terms[0]
    if len(terms) == 1:
        return running_total == expected
    return mult(expected, running_total, terms[1:]) or add(expected, running_total, terms[1:])


def arrangeable(expected, terms):
    if len(terms) == 0:
        return False
    return mult(expected, 1, terms) or add(expected, 0, terms)

if __name__ == "__main__":
    total = 0
    for line in iter(input, ''):
        expected_str, terms = line.strip().split(': ')
        expected = int(expected_str)
        if arrangeable(expected, [int(x) for x in terms.split()]):
            total += expected
    print(total)
