"""
Title     : Mod Divmod
Subdomain : Math
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/python-mod-divmod/problem
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
d = divmod(a, b)
print(d[0])
print(d[1])
print(d)