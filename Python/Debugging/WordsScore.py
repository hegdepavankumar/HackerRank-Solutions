"""
Title     : Words Score
Subdomain : Debugging
Domain    : Python
Author    : Pavankumar Hegde
Problem   : https://www.hackerrank.com/challenges/words-score/problem
"""
# Solution



def is_vowel(letter):
    return letter in ["a", "e", "i", "o", "u", "y"]


def score_words(words):
    score = 0
    for word in words:
        num_vowels = sum(1 for letter in word if is_vowel(letter))
        score += 2 if num_vowels % 2 == 0 else 1
    return score