#!/usr/bin/env python3

from dataclasses import dataclass
import re

@dataclass
class Token:
    type: str
    value: str

def tokenize(rules, text):
    tokens = []
    pos = 0

    compiled_rules = [(name, re.compile(pattern)) for name, pattern in rules]

    while pos < len(text):
        match = None

        for token_name, pattern in compiled_rules:
            match = pattern.match(text, pos)

            if match:
                value = match.group(0)
                tokens.append(Token(token_name, value))
                pos = match.end()
                break

        if not match:
            raise ValueError(f"Invalid character at position {pos}: {text[pos]}")

    return tokens

def extract_multiples(tokens):
    pairs = []
    enabled = True
    for i, token in enumerate(tokens):
        if i + 5 >= len(tokens):
            break

        if (token.type == 'do') and (tokens[i + 1].type == 'lparen') and (tokens[i + 2].type == 'rparen'):
            enabled = True
            continue

        if (token.type == 'dont') and (tokens[i + 1].type == 'lparen') and (tokens[i + 2].type == 'rparen'):
            enabled = False
            continue

        if not enabled:
            continue
        
        if token.type != 'multiply':
            continue
        if tokens[i + 1].type != 'lparen':
            continue
        if tokens[i + 2].type != 'int':
            continue
        if tokens[i + 3].type != 'comma':
            continue
        if tokens[i + 4].type != 'int':
            continue
        if tokens[i + 5].type != 'rparen':
            continue
        pairs.append((int(tokens[i + 2].value), int(tokens[i + 4].value)))

    return pairs

def apply_multiplication(tuples):
    return sum(a * b for a,b in tuples)

if __name__ == "__main__":
    import fileinput

    rules = [
        ('multiply', 'mul'),
        ('dont', "don't"),
        ('do', 'do'),
        ('lparen', r'\('),
        ('rparen', r'\)'),
        ('int', r'\d+'),
        ('comma', ','),
        ('ignore', '.')
    ]

    for line in fileinput.input():
        tokenized = tokenize(rules,line.strip())
        multiplication_candidates = extract_multiples(tokenized)
        print(apply_multiplication(multiplication_candidates))
