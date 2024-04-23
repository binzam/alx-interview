#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    Recursively calculates the minimum number of operations to go
    from one 'H' to n 'H's if the only available operations are
    "Copy All" and "Paste"
    """
    if n <= 1:
        return 0

    for i in range(2, int((n / 2) + 1)):
        if n % i == 0:
            return minOperations(int(n / i)) + i

    return n
