"""
Title     : itertools.combinations_with_replacement()
Subdomain : Itertools
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
"""

# Solution:


from itertools import *

s, n = input().split()
n = int(n)
s = sorted(s)
for j in combinations_with_replacement(s, n):
    print("".join(j))