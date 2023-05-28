"""
Title     : Exceptions
Subdomain : Errors and Exceptions
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/exceptions/problem
"""


# Solution


n = int(input())
for _ in range(n):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except Exception as e:
        print(f"Error Code: {e}")