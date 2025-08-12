import numpy as np


def func(x):
    """
    This function takes one arguments x and returns its power of two.
    """
    return x**2


def INPUT_MATRIX() -> tuple[list[list[int]], int]:
    """
    This function reads input from the user and returns a list of lists of integers.
    The first line contains two integers N and M, where N is the number of lists and M is the modulo value.
    The next N lines each contain a list of integers.
    """
    N, M = map(int, input().split())
    arrays = []
    for i in range(N):
        m = list(map(int, input().split()))
        arrays.append(m[1:])
    return arrays, M


def maximizeIt(arrays, M):
    # Apply func to every element in each list
    for idx in range(len(arrays)):
        arrays[idx] = list(map(func, arrays[idx]))

    # Start with remainder 0
    reachable = {0}

    # this will get me all possible remainders and i can get the max in the end it takes frist the len loop of arrays
    # and then the second loop of the values in the set
    # finally through each array and calculate reachable remainders
    for arr in arrays:
        new_reachable = set()
        for r in reachable:
            for val in arr:
                new_reachable.add((r + val) % M)
        reachable = new_reachable

    return max(reachable)


if __name__ == "__main__":

    print("Enter the number of lists and modulo value (N M):")

    print(maximizeIt(*INPUT_MATRIX()))
