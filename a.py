#!/usr/bin/python3

import sys

def factorize(num):
    """numbers to be factorised"""

    factors = []
    for i in range(2, num):
        if num % i == 0:
            factors.append((i, int(num / i)))
    return (factors)

if len(sys.argv) != 2:
    print("Error: failed to open")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r') as file:
        for line in file:
            num = int(line.strip())
            factors = factorize(num)
            for factor in factors:
                print("{:.0f}={:.0f}*{:.0f}".format(num, factor[0], factor[1]))
except FileNotFoundError:
    print("File not Found.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
