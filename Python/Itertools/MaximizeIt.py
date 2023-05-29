"""
Title     : Maximize It!
Subdomain : Itertools
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/maximize-it/problem
"""

# Solution:

import itertools

k, m = map(int, input().split())

main_ar = []
for _ in range(k):
    ar = list(map(int, input().split()))
    main_ar.append(ar[1:])

all_combination = itertools.product(*main_ar)
result = 0
for single_combination in all_combination:
    result = max(sum(x * x for x in single_combination) % m, result)
print(result)