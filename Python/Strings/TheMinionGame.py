"""
Title     : The Minion Game
Subdomain : Strings
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/the-minion-game/problem
"""

# Solution


s = input().strip()
s_length = len(s)
vowel_list = ["A", "E", "I", "O", "U"]
stuart_point = 0
kevin_point = 0
for i in range(s_length):
    if s[i] in vowel_list:
        kevin_point += s_length - i
    else:
        stuart_point += s_length - i
if stuart_point == kevin_point:
    print("Draw")
elif kevin_point > stuart_point:
    print("Kevin", kevin_point)
else:
    print("Stuart", stuart_point)