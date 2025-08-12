"""
this script use regex to replace all non-alphanumeric characters between alphanumeric characters with a single space
"""

import re


def replace_non_alphanumeric_with_space(n, m):
    """Replace non-alphanumeric characters between alphanumeric characters with a single space."""
    for i in range(n * m):
        inpuStr += input()
    outputStr = re.sub(r"(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])", " ", inputStr)
    return outputStr


if __name__ == "__main__":
    inputStr = ""
    n = int(input())
    m = int(input())
    print(replace_non_alphanumeric_with_space(n, m))
