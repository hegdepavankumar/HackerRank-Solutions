"""
Title     : Capitalize!
Subdomain : Strings
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/capitalize/problem
"""

# Solution


s = input()
s_ar = s.split(" ")
final_ar = []
space = " "
for w in s_ar:
    final_ar.append(w.capitalize())
print(space.join(final_ar))