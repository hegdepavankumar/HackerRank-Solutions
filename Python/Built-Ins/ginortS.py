"""
Title     : ginortS
Subdomain : Built-Ins
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/ginorts/problem
"""


# Solution


s = input()
print(
    "".join(
        sorted(
            s,
            key=lambda x: (
                x.isdigit() and int(x) % 2 == 0,
                x.isdigit(),
                x.isupper(),
                x.islower(),
                x,
            ),
        )
    )
)