"""
Title     : collections.Counter()
Subdomain : Collections
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/collections-counter/problem
"""


# Solution:


x = int(input())
shoe_size = list(map(int, input().split()))
n = int(input())
sell = 0
for _ in range(n):
    s, p = map(int, input().split())
    if s in shoe_size:
        sell = sell + p
        shoe_size.remove(s)
print(sell)