"""
DART GAME

The score calculation logic follows below.

1. A player is given three chances.
2. For each attempt, a player can achieve 10 points maximum.
3. On the board there are areas Single(S), Double(D), Triple(T) exist, and when a player hit the area,
   the player can get score^1 for Single(S), score^2 for Double(D), score^3 for Triple(T).
4. There are other options; Star(*) and Oops(#).
    a. When a player gets Star(*), the previous score becomes score * 2.
    b. When a player gets Oops(#), the previous score becomes score * 2 and will be subtracted from the total score.
    c. When a player gets Star(*) and then gets Star(*) or Oops(#) for the next attempt,
       the previous score will be doubled once again.
       For example, like in the 4th case below, with the input "1S*2T*3S", the player will get 1 * 2 * 2 = 4 points.
5. The Star(*) can be achieved even for the first attempt.
   In that case, the first score the player achieved will be doubled.
6. Single(S), Double(D), Triple(T) does exist for each attempt.
7. Star(*) and Oops(#) can exist one at a time, and it is also possible to not exist.

Return the total score with the input which consists of integers between 0 and 10 and characters S, D, T, *, #.



Input Format:
A string that consists of three of the score/bonus/option combination.

Examples
No  dartResult	answer	설명
 1  1S2D*3T    37	    1^1 * 2 + 2^2 * 2 + 3^3
 2  1D2S#10S   9	    1^2 + 2^1 * (-1) + 10^1
 3  1D2S0T	   3	    1^2 + 2^1 + 0^3
 4	 1S*2T*3S	23	    1^1 * 2 * 2 + 2^3 * 2 + 3^1
 5	 1D#2S*3S   5	    1^2 * (-1) * 2 + 2^1 * 2 + 3^1
 6	 1T2D3D#	   -4	    1^3 + 2^2 + 3^2 * (-1)
 7	 1D2S3T*	   59	    1^2 + 2^1 * 2 + 3^3 * 2
"""


def solution(dartResult):
    bonuses = {"S": 1, "D": 2, "T": 3}
    options = {"*": 2, "#": -1}
    scores_stack = []

    dartResult = dartResult.replace("10", "@")

    for i in dartResult:
        if i.isdigit() or i == "@":
            scores_stack.append(10 if i == "@" else int(i))

        elif i in bonuses:
            curr_score = scores_stack.pop()
            scores_stack.append(curr_score ** bonuses[i])

        elif i in options:
            if i == "#":
                scores_stack[-1] *= options[i]
            elif i == "*":
                curr_score = scores_stack.pop()
                if len(scores_stack):
                    scores_stack[-1] *= options[i]
                scores_stack.append(curr_score * options[i])

    return sum(scores_stack)


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))


# bonuses = {"S": 1, "D": 2, "T": 3}
# print(bonuses["S"])
