"""
Title     : Input()
Subdomain : Built-Ins
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/input/problem
"""


# Solution


if __name__ == "__main__":
    x, k = map(int, input().strip().split())
    equation = input().strip()
    print(eval(equation) == k)
    