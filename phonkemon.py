"""
Original Test Question: https://programmers.co.kr/learn/courses/30/lessons/1845

You are given an array of integers of N elements.
There may be duplicate elements in the array.
You can pick up N/2 elements from the array.
Implement a function that returns the maximal number of elements you can pick up.


Constraints:
- nums: 1 dimensional array that includes integers.
- 1 <= The length of nums <= 10,000
- The length of nums is even.
- 1 <= The elements of nums <= 200,000


Example 1
nums: [3, 1, 2, 3], result: 2

Example 2
nums: [3, 3, 3, 2, 2, 4], result: 3

Example 3
nums: [3, 3, 3, 2, 2, 2], result: 2
"""

nums = [3, 3, 3, 2, 2, 4]


def solution(nums):
    set_nums = set(nums)
    answer = 0

    if len(nums)/2 >= len(set_nums):
        print(len(set_nums))
        answer = len(set_nums)
    else:
        print(len(nums)/2)
        answer = len(nums)/2

    return answer


solution(nums)
