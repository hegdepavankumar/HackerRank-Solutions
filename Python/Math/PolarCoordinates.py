"""
Title     : Polar Coordinates
Subdomain : Math
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/polar-coordinates/problem
"""
import cmath

z = complex(input())
p = cmath.polar(z)
print(p[0])
print(p[1])