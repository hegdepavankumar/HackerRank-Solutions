"""
Title     : Default Arguments
Subdomain : Debugging
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/default-arguments/problem
"""
# Solution
# Enter your code here. Read input from STDIN. Print output to STDOUT

def print_from_stream(n, stream=EvenStream()):
    stream.__init__()
    for _ in range(n):
        print(stream.get_next())