"""
Original Test Question: https://programmers.co.kr/learn/courses/30/lessons/12982

Budgeting

Within the limited budget, you need to distribute in the way of maximizing the number of offices which can get budget.

When you distribute the budget, you must distribute the budget as much as the requested amount of budget.
You cannot discount the requested budget amount.
For example, if office A requested & 1,000, you need to give $ 1,000 to office A.
If you do not have enough budget, then you simply cannot give the money.

You will receive parameter "d" which includes the information of budget requests,
and another parameter "budget" which includes the total amount of money.
You need to return the maximum number of offices which can get budget.


Constraints:
1. 1 <= the length of d <= 100
2. 1 <= d[i] <= 10,000,000
3. d[i] are natural numbers.


Example
d                   budget  result
[1, 3, 2, 5, 4]     9       3
[2, 2, 3, 3]        10      4
"""


# # Time exceeded solution. Works but not efficient.
# from itertools import combinations
#
#
# def solution(d, budget):
#     answer = 0
#     office_to_be_budgeted = 0
#
#     d.sort()
#
#     for i in range(1, len(d) + 1):
#         for j in combinations(d, i):
#             if sum(j) > budget:
#                 break
#             else:
#                 if office_to_be_budgeted <= len(j):
#                     office_to_be_budgeted = len(j)
#                     answer = office_to_be_budgeted
#                 else:
#                     continue
#
#     return answer


# A better solution.
def solution(d, budget):
    d.sort()

    while sum(d) > budget:
        d.pop()

    return len(d)


d = [2, 2, 2, 3, 10, 2, 4, 7, 9, 10, 11, 21, 19, 1, 1, 3, 6]
budget = 30

# d = [5, 3, 2, 4, 1]
# budget = 10

print(solution(d, budget))
