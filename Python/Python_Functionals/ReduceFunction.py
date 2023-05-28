"""
Title     : Reduce Function
Subdomain : Python Functionals
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/reduce-function/problem
"""

# Solution:


from fractions import Fraction
from functools import reduce


def product(fracs):
    t = Fraction(reduce(lambda x, y: x * y, fracs))
    return t.numerator, t.denominator


if __name__ == "__main__":
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

"""
3
1 2
3 4
10 6
"""