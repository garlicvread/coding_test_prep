"""
Failure Rate: https://programmers.co.kr/learn/courses/30/lessons/42889

The failure rate is defined as follows.

1. The number of players who reached the stage but not cleared it / the number of players who reached the stage

When two parameters such as N (the number of stages) and stages (the current stage the player is staying) are given,
we need to return the list of stages in descending order of failure rate.


Constraints
1. 1 <= the number of "stages" <= 50, natural number.
2. 1 <= the length of "stages" <= 200,000, natural number.
3. 1 <= The elements of "stages" <= N + 1, natural number.
4. Each natural number means the stage the player is challenging.
5. N + 1 means the player cleared all the stages (up to Nth stage).
6. When there is no players who reached a stage, the failure rate of the stage is 0.
7. When the failure rate are the same between different stages,
   the stage with smaller stage number should be listed first.


Example
N    stages                      result
5    [2, 1, 2, 6, 2, 4, 3, 3]    [3, 4, 2, 1, 5]
4    [4, 4, 4, 4, 4]             [4, 1, 2, 3]


Explanations
The parameter "stages" consists if numbers.
Each number means the stage number where each player is now staying.

In the first example, the stages is [2, 1, 2, 6, 2, 4, 3, 3].
This means that
the first player is now in the second stage,
the second player is now in the first stage,
the third player is now in the second stage,
the fourth player is now in the sixth stage,
the fifth player is now in the second stage,
the sixth player is now in the fourth stage,
the seventh player is now in the third stage,
and the eighth player is now in the third stage.

Thus:
At stage 1, 8 players challenged and 1 player could not clear the stage. Thus, the failure rate is 1/8.
At stage 2, 7 players challenged and 3 player could not clear the stage. Thus, the failure rate is 3/7.
Likewise, the failure rate of rest of the stages are:
stage 3: 2/4
stage 4: 1/2
stage 5: 0/1

Thus, the return value is [3, 4, 2, 1, 5]


For case 2
All players are staying at the last stage, thus the failure rate is 1.
The rest of the stages are the same which is 0.
The return value is [4, 1, 2, 3]
"""


def solution(N, stages):
    answer = []
    players_at = {}  # A dictionary to store the number of players who are staying at a certain stage.
    dividers = []
    failure_rate = {}

    for i in range(len(stages)):
        for j in range(1, N + 1):
            if stages[i] == j:
                if j in players_at:
                    players_at[j] += 1
                else:
                    players_at[j] = 1
    # print("players_at: ", players_at)

    # If a certain stage does not exist, add the stage number as the key and 0 as the value.
    for i in range(1, N + 1):
        if i not in players_at:
            players_at[i] = 0
    # print("modified players_at:", players_at)

    # Sort players_at dictionary by the key.
    sorted_players_at = sorted(players_at.items(), key=lambda x: x[0])
    # print("sorted players_at:", sorted_players_at)

    # Fill the dividers
    for i in range(len(sorted_players_at)):
        if i == 0:
            dividers.append(len(stages))
        else:
            dividers.append(dividers[-1] - sorted_players_at[i - 1][1])

    # print("dividers:", dividers)

    # Calculate the failure rate
    for i in range(len(sorted_players_at)):
        try:
            failure_rate[sorted_players_at[i][0]] = sorted_players_at[i][1] / dividers[i]
        except ZeroDivisionError:
            failure_rate[sorted_players_at[i][0]] = 0

    # print("failure_rate:", failure_rate)

    # Sort failure_rate dictionary by the value.
    sorted_failure_rate = sorted(failure_rate.items(), key=lambda x: x[1], reverse=True)
    # print("sorted_failure_rate:", sorted_failure_rate)

    # Store the keys to answer.
    for i in range(len(sorted_failure_rate)):
        answer.append(sorted_failure_rate[i][0])

    return answer


# # Alternative solution 1
# def solution(N, stages):
#     result = {}
#     denominator = len(stages)
#     for stage in range(1, N+1):
#         if denominator != 0:
#             count = stages.count(stage)
#             result[stage] = count / denominator
#             denominator -= count
#         else:
#             result[stage] = 0
#     return sorted(result, key=lambda x : result[x], reverse=True)


# # Alternative solution 2
# def solution(N, stages):
#     fail = {}
#     for i in range(1,N+1):
#         try:
#             fail_ = len([a for a in stages if a==i])/len([a for a in stages if a>=i])
#         except:
#             fail_ = 0
#         fail[i]=fail_
#     answer = sorted(fail, key=fail.get, reverse=True)
#     return answer


# # Alternative solution 3
# def solution(N, stages):
#     answer = []
#     fail = []
#     info = [0] * (N + 2)
#     for stage in stages:
#         info[stage] += 1
#     for i in range(N):
#         be = sum(info[(i + 1):])
#         yet = info[i + 1]
#         if be == 0:
#             fail.append((str(i + 1), 0))
#         else:
#             fail.append((str(i + 1), yet / be))
#     for item in sorted(fail, key=lambda x: x[1], reverse=True):
#         answer.append(int(item[0]))
#     return answer


# Test code
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
