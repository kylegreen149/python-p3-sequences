#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = []
    if length == 0:
        fibonacci = []
    if length == 1:
        fibonacci = [0]
    if length > 1:
        fibonacci = [0, 1]

    while len(fibonacci) < length :
        total = fibonacci[-2] + fibonacci[-1]
        fibonacci.append(total)
    print(fibonacci)