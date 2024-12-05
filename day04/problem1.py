#!/usr/bin/env python3

def rotate_90(lines):
    result = []

    for row_index, line in enumerate(lines):
        for col_index, char in enumerate(line):
            if len(result) <= col_index:
                result.append('')
            result[col_index] = result[col_index] + char
    return result

def rotate_45(lines):
    if len(lines) == 0:
        return []

    line_length = len(lines[0])
    result = [[' '] * line_length for _ in range(line_length + len(lines) - 1)]

    for col_index in range(line_length):
        for row_index in range(len(lines)):
            result[row_index + col_index][col_index] = lines[row_index][col_index]

    return [''.join(chars) for chars in result]

def rotate_315(lines):
    if len(lines) == 0:
        return []

    line_length = len(lines[0])
    result = [[' '] * line_length for _ in range(line_length + len(lines) - 1)]

    for col_index in range(line_length):
        for row_index in range(len(lines)):
            result[row_index + (line_length - 1 - col_index)][col_index] = lines[row_index][col_index]

    return [''.join(chars) for chars in result]

def count_matches(needle, haystack):
    other_needle = needle[::-1]
    return sum((line.count(needle) + line.count(other_needle)) for line in haystack)

if __name__ == "__main__":
    import fileinput

    lines = []
    for line in fileinput.input():
        lines.append(line.strip())

    puzzles = [lines, rotate_45(lines), rotate_90(lines), rotate_315(lines)]

    answer = sum(count_matches('XMAS', haystack) for haystack in puzzles)
    print(answer)
