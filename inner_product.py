"""
The Original Test Question: https://programmers.co.kr/learn/courses/30/lessons/70128

Calculate the inner product (dot product) of two vectors.
The two vectors are 1 dimensional arrays and have same length.


Constraints:
- 1 <= The length of the two vectors <= 1,000
- -1,000 <= The elements of the vectors <= 1,000


Example 1
a: [1, 2, 3, 4], b: [-3, -1, 0, 2], result: 3
a: [-1, 0, 1], b: [1, 0, -1], result: -2
"""


def solution(a, b):
    answer = 0

    for i in range(len(a)):
        answer += a[i] * b[i]

    return answer
