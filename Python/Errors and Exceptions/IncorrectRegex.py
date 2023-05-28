"""
Title     : Incorrect Regex
Subdomain : Errors and Exceptions
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/incorrect-regex/problem
"""


# Solution



import re

n = int(input())
for _ in range(n):
    s = input()
    try:
        re.compile(s)
        print(True)
    except Exception as e:
        print(False)
        