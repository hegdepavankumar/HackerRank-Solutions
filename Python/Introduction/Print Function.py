""" 
Title     : Print Function
Subdomain : Introduction
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/python-print/problem

"""

# Solution 1

if __name__ == "__main__":
    n = int(input())
    ar = range(1, n + 1)
    for i in ar:
        print(i, end="")

# Solution 2

"""
Alternate solution:

if __name__ == '__main__':
    n = int(input())
    print("".join([str(i) for i in range(1,n+1)]))

"""