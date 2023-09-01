#!/usr/bin/python3

import sys

if __name__ == "__main__":
    from fact import factorize

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
                    print(f"{num} = {factor[0]} * {factor[1]}")
    except FileNotFoundError:
        print("File not Found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
