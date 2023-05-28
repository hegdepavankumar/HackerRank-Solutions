""" 
Title     : Tuples
Subdomain : Basic Data Types
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/python-tuples/problem

"""


# Solution

if __name__ == "__main__":
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))