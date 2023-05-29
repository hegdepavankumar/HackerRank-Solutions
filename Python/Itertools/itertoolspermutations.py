"""
Title     : itertools.permutations()
Subdomain : Itertools
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/itertools-permutations/problem
"""

# Solution:


import itertools

s, n = list(map(str, input().split(" ")))
s = sorted(s)
for p in list(itertools.permutations(s, int(n))):
    print("".join(p))