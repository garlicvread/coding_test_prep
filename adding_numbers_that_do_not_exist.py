"""
Original Test Question: https://programmers.co.kr/learn/courses/30/lessons/86051

An integer array "numbers" that includes some random integers from 0 to 9 is given.
Sum all the missing numbers from the array, and return it.


Conditions:
- 1 ≤ length of "numbers" ≤ 9
- 0 ≤ each element of "numbers" ≤ 9
- The elements of "numbers" are different from each other.


Example 1:
numbers: [1, 2, 3, 4, 6, 7, 8, 0]
result: 14


Example 2:
numbers: [5,8,4,0,6,7,9]
result: 6
"""


# def solution(numbers):
#     answer = -1
#     return answer

numbers = [1, 2, 3, 4, 6, 7, 8, 0]


def solution(numbers):
    list_to_compare = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sum_of_missing_numbers = 0

    for i in range(len(list_to_compare)):
        if list_to_compare[i] not in numbers:
            sum_of_missing_numbers += list_to_compare[i]

    answer = sum_of_missing_numbers
    # print(answer)
    return answer


solution(numbers)
