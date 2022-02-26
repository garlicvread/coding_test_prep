"""
Original Test Question: https://programmers.co.kr/learn/courses/30/lessons/76501

A parameter "absolutes" contains the absolute values of some integers.
A parameter "sings" contains the signs of the integers as boolean values.
You need to calculate the actual sum of the integers with the solution function.


Conditions:
1. 1 <= The length of absolutes <= 1000
2. The length of signs == the length of absolutes.
3. When signs[i] are True, then the actual value of absolutes[i] are positive integers and vice versa.


Examples
absolutes	    signs	                result
[4, 7, 12]	    [true, false, true]	    9
[1, 2, 3]	    [false, false, true]	0


For example 1:
The signs is [true, false, true] so the actual value is 4, -7, 12 respectively.
Thus, you need to return the sum of three integers and the result is 9.

For example 2:
The signs is [false, false, true] so the actual value is -1, -2, 3 respectively.
Thus, you need to return the sum of three integers and the result is 0.
"""


def solution(absolutes, signs):
    """
    param absolutes: list of integers
    param signs: list of boolean values
    return: sum of integers
    """
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer


solution([4, 7, 12], [True, False, True])


# # Alternative Code
# def solution(absolutes, signs):
#     return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
