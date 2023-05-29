"""
Title     : Linear Algebra
Subdomain : Numpy
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/np-linear-algebra/problem
"""

import numpy as np

np.set_printoptions(legacy="1.13")
n = int(input())
array = np.array([input().split() for _ in range(n)], float)
print(np.linalg.det(array))