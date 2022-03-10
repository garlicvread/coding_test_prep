"""
Original Test Question: https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3

Returning the middle character

We are given a string.
With the string, we will return the character which is placed in the middle of the string.

If the string is odd, we will return the middle character.
If the string is even, we will return the middle two characters.


Constraints
1. 1 <= length of string <= 100


Example
s          return
"abcde"    "c"
"qwer"     "we"
"""


def solution(s):
    answer = ""
    if len(s) % 2 == 0:
        answer = s[len(s) // 2 - 1:len(s) // 2 + 1]
    else:
        answer = s[len(s) // 2]
    return answer


# # Alternative Solution 1
# def solution(s):
#     return s[(len(s) - 1) // 2 : len(s) // 2 + 1]
#
#
# # Alternative Solution 2
# def string_middle(str):
#     a = len(str)
#     if a % 2 == 0:
#         a = (a-2) / 2
#     else :
#         a = (a-1) / 2
#     return str[int(a): -int(a)]
#
#
# # Alternative Solution 3
# solution = lambda s: s[(len(s) - 1) // 2 : len(s) // 2 + 1]
