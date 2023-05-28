"""
Title     : Zipped!
Subdomain : Built-Ins
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/zipped/problem
"""

# Solution


N, X = map(int, input().split())
scores = []
for _ in range(X):
    scores.append(list(map(float, input().split())))
for i in zip(*scores):
    print(sum(i) / len(i))