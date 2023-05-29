"""
Title     : Set .add()
Subdomain : Sets
Domain    : Python
Author    : Pavankumar Hegde
problem   : https://www.hackerrank.com/challenges/py-set-add/problem
"""

n = int(input())
country_set = set()
for _ in range(n):
    country_name = input()
    country_set.add(country_name)
print(len(country_set))