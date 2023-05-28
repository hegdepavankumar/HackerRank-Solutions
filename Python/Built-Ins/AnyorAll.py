"""
Title     : Any or All
Subdomain : Built-Ins
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/any-or-all/problem
"""


# Solution


n = input()
ar = input().split()
print(all(int(i) > 0 for i in ar) and any(i == i[::-1] for i in ar))