"""
Original Test Question: https://programmers.co.kr/learn/courses/30/lessons/12906

Removing consecutive duplicates

With the array given, we need to remove consecutive duplicates.
For example, if array = [1, 1, 3, 3, 0, 1, 1] then we need to return [1, 3, 0, 1].
And if arr = [4, 4, 4, 3, 3] then the return must be [4, 3].

Note that in this case, the numbers in the return should follow the order of the original array.

Constraints:
1. 1 <= len(arr) <= 1,000,000, natural number.
2. 0 <= The elements of the inputted array <= 9, natural number.
"""


def solution(arr):
    if len(arr) == 0:
        return []

    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            result.append(arr[i])
    return result


arr = [1, 1, 3, 3, 0, 1, 1]
print(solution(arr))
