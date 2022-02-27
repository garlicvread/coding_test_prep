"""
Original Test Question: https://programmers.co.kr/learn/courses/30/lessons/72410

Let's assume that you are playing a lottery.
The lottery you are playing sets winner cases as follows.

    1st: All 6 numbers are matched.
    2nd: 5 numbers are matched.
    3rd: 4 numbers are matched.
    4th: 3 numbers are matched.
    5th: 2 numbers are matched.
    6th: Any other cases.

The order of the numbers does not matter.


Let's assume that some numbers on your lottery ticket are erased.
If you mark the erased numbers as 0, then your number can be 44, 1, 0, 0, 31 25.

If the winning numbers are 31, 10, 45, 1, 6, 19, the possible best and worst cases are the same as follows.

Winning Numbers: 31 10 45 1 6 19

The Best Case: 31 0→1 44 0→6 25: 4 numbers are matched. 3rd position.
The Worst Case: 31 0→11 44 0→7 25: 2 numbers are matched. 5th position.


The input parameters are:
lottos: the number on your lottery ticket.
win_nums: the winning numbers.

The output should include the best possible position and the worst possible position in the order.


Constraints:
- lottos: An int array. The length of lottos is 6.
- All elements of lottos have a range between 0 and 45.
- 0 is the erased number.
- Except for 0, the other numbers are included only once in the lottos array.
- The elements of lottos may not be sorted.

- win_nums: An int array. The length of win_nums is 6.
- All elements of win_nums have a range between 1 and 45.
- There are no same numbers in win_nums. Every number includes only once.
- The elements of win_nums may not be sorted.


Example input 1:
lottos: [44, 1, 0, 0, 31, 25]
win_nums: [31, 10, 45, 1, 6, 19]

Example output 1:
result: [3, 5]


Example input 2:
lottos: [0, 0, 0, 0, 0, 0]
win_nums: [38, 19, 20, 40, 15, 25]

Example output 2:
result: [1, 6]


Example input 3:
lottos: [45, 4, 35, 20, 3, 9]
win_nums: [20, 9, 3, 45, 4, 35]

Example output 3:
result: [1, 1]
"""


def solution(lottos, win_nums):
    count_zero = lottos.count(0)
    count_same = 0

    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            count_same += 1

    best_case = 7 - (count_same + count_zero) if count_same + count_zero > 0 else 6
    worst_case = 7 - count_same if count_same > 0 else 6

    answer = [best_case, worst_case]

    return answer


lottos = [0, 0, 0, 0, 0, 0]
win_nums = [31, 10, 45, 1, 6, 19]

solution(lottos, win_nums)  # [1, 6]
