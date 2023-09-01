#!/bin/usr/python3

"""factoris of numbers"""


def factorize(num):
    """numbers to be factorised"""

    factors = []
    for i in range(2, num):
        if num % i == 0:
            factors.append((i, int(num / i)))
    return (factors)
