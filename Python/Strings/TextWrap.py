"""
Title     : Text Wrap
Subdomain : Strings
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/text-wrap/problem
"""

# Solution


import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)