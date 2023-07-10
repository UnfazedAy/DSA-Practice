#!/usr/bin/python3

# Given a sentence a and word b, find the number of times b occurs in a.
# The repeated words should be concatenated and next to each other.

"""
Example:
Input: a = "popokpo" b = "po"
Output: 2
Explanation: The word "po" is repeated twice and concatenated as 'popo' in "popokpo
a and b will only contain lowercase letters
"""


def solution(a: str, b: str):
    # Write your solution here
    a_length = len(a)
    arr = [b * i for i in range(1, a_length + 1)]

    count = 0
    for word in arr:
        if word in a:
            count += 1
    return count


if __name__ == "__main__":
    a = input()
    b = input()
    output = solution(a, b)
    print(output)
