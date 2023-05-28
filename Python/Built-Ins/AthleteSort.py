"""
Title     : Athlete Sort
Subdomain : Built-Ins
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/python-sort-sort/problem
"""


# Solution


if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    for i in sorted(arr, key=lambda x: x[k]):
        print(*i)