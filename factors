#!/usr/bin/python3

from sys import argv


def factorize(num):
    """"find two small numbers that multiply to give a given number"""
    i = 2

    if num < 2:
        return

    while num % i:
        i += 1
    print("{:.0f}={:.0f}*{:.0f}".format(num, num / i, i))

if len(argv) != 2:
    exit()

try:
    with open(argv[1]) as file:
        line = file.readline()

        while line != "":
            numb = int(line.split('\n')[0])
            factorize(num)
            line = file.readline()
except:
    pass
