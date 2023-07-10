#!/usr/bin/env python3

# You are given a string s and an integer array k of the same length. The string s will be randomly sorted
# such that each character at the jth position gets moved to k[j] in the sorted string.

"""
Example:
Input: s = "talentcloudturing", k = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 0, 1, 2, 3, 4, 5]
output: "turingtalentcloud"
Explanation: The characters in string s are shifted to their new positions according to the values in k
"""


def solution(s: str, k: list[int]) -> str:
    """
    A function that takes in a string and an integer array and returns a string
    """
    for i in range(len(k)):
        # convert the string to an integer before using it as an index
        k[i] = int(k[i])
        k[i] = s[k[i]]

    return "".join(s)


if __name__ == "__main__":
    s = input()
    line = input()
    k = line.strip().split()
    output = solution(s, k)
    print(output)
