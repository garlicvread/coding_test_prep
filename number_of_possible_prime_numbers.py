"""
Original Test Question: https://programmers.co.kr/learn/courses/30/lessons/12977

When summing up the given three numbers, check how many cases to be a prime number exist.

"nums" is The parameter that includes numbers.
The number of elements has a range between 3 and 50.

Check how many prime number is possible
when picking up random three numbers and adding them together from the array "nums".

Return the number of possible prime numbers.


Conditions:
1. 3 <= The number of elements in nums <= 50
2. 1 <= Each element of nums <= 1000
3. Each element of nums is a natural number.
4. There is no duplication in the array nums.


Example:
nums	        result
[1,2,3,4]	    1
[1,2,7,6,4]	    4


For the first example, you can make 7 using [1,2,4].

For the second example, you can make
    7 using [1,2,4].
    11 using [1,4,6].
    13 using [2,4,7].
    17 using [4,6,7].
"""


from itertools import combinations


def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        if isPrime(sum(i)):
            answer += 1
    print(answer)
    return answer
