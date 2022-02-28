"""
Original Test Question: https://programmers.co.kr/learn/courses/30/lessons/67256

Let's assume that the keypad of a smartphone looks like the following.

    1   2   3
    4   5   6
    7   8   9
    *   0   #

You are going to tab only the numbers, only with your thumbs.
The starting position of the left thumb is * and of the right thumb is #.

Your thumb can move upward, downward, leftward, and rightward.
The distance between the two attached keypads is 1.

You can touch the most left column 1, 4, 7 with your left thumb,
and for the most right column 3, 6, 9 with your right thumb.
For the middle column, 2, 5, 8, 0, you must touch the keypad with your closest thumb.

If the distance between the current Numpad and your left and right thumbs,
if you are a right-handed person, touch it with your right thumb.
Otherwise, tap it with your left thumb.

The parameter "numbers" contains the keypad you need to tap in order.
The parameter "hand" contains the information of which hand you are using.

You need to return which hand was used when you push the keypad.
The returned value should be a concatenated string.


Constraints:
- 1 <= The size of "numbers" array <= 1000
- 0 <= The elements the "numbers" array include <= 9
- hand: "left" or "right"
- Return a concatenated string that consists of L for your left thumb and R for your right thumb.


Example
numbers                             hand	    result
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	    "LRLLLRLLRRL"
[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	    "LRLLRRLLLRR"
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	    "right"	    "LLRLLRLLRL"


For the first example:
The order of pushing numpad is [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], and you are a right-handed person.

Left    Right   Number  Used
Thumb   Thumb   to Tab  Hand
*	    #	    1	    L	    1: left thumb
1	    #	    3	    R	    3: right thumb
1	    3	    4	    L	    4: left thumb
4	    3	    5	    L	    Distance to left thumb is 1 and to right Thumb is 2: use left thumb
5	    3	    8	    L	    Distance to left thumb is 1 and to right Thumb is 3: use left thumb
8	    3	    2	    R	    Distance to left thumb is 2 and to right Thumb is 1: use right thumb
8	    2	    1	    L	    1: left thumb
1	    2	    4	    L	    4: left thumb
4	    2	    5	    R	    Distance to both thumbs are the same, so use the right thumb
4	    5	    9	    R	    9: right thumb
4	    9	    5	    L	    Distance to left thumb is 1 and to right Thumb is 2: use left thumb
5	    9	    -	    -

The return will be "LRLLLRLLRRL".


For the second example:
    If a left-handed person pushes [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2] respectively,
    the return should be "LRLLRRLLLRR".


For the third example:
    If a right-handed person pushes [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] respectively,
    the return should be "LLRLLRLLRL".
"""


def solution(numbers, hand):

    # Numpad matrix:
    numpads = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9],
               ["*", 0, "#"]]

    current_left_thumb = [3, 0]  # Current left thumb position
    current_right_thumb = [3, 2]  # Current right thumb position

    current_position = []  # The last numpad that you touched

    count = 0  # Count the number of times you touched the numpad
    distance = 0  # Distance between the current numpad and the left or right thumb

    answer = []  # The order of the left or right thumb you used

    for i in range(len(numbers)):
        for j in range(len(numpads)):
            for k in range(len(numpads[j])):
                if numbers[i] == numpads[j][k]:
                    print(numpads[j][k], " - ", j + 1, "행", k + 1, "열")

                    current_position.append([j, k])
                    count += 1

                    print("STEP:", count)
                    print("POS:", current_position)
                    print("CURR:", current_position[-1])

                    l_distance = abs(current_left_thumb[0] - current_position[-1][0]) + \
                                 abs(current_left_thumb[1] - current_position[-1][1])

                    r_distance = abs(current_right_thumb[0] - current_position[-1][0]) + \
                                 abs(current_right_thumb[1] - current_position[-1][1])

                    if numbers[i] in [1, 4, 7]:
                        current_left_thumb = current_position[-1]
                        distance = l_distance  # There's no need to calculate the distance in this stage.
                        answer.extend("L")
                        print("answer", answer, " '1' ")
                        print("DISTANCE:", distance, "\n")
                    elif numbers[i] in [3, 6, 9]:
                        current_right_thumb = current_position[-1]
                        distance = r_distance  # There's no need to calculate the distance in this stage.
                        answer.extend("R")
                        print("answer", answer, " '2' ")
                        print("DISTANCE:", distance, "\n")
                    else:
                        if l_distance == r_distance:
                            if hand == "right":
                                current_right_thumb = current_position[-1]
                                distance = r_distance
                                answer.extend("R")
                                print("answer", answer, " '3' ")
                                print("DISTANCE:", distance, "\n")
                            else:
                                current_left_thumb = current_position[-1]
                                distance = l_distance
                                answer.extend("L")
                                print("answer", answer, " '4' ")
                                print("DISTANCE:", distance, "\n")
                        elif l_distance < r_distance:
                            current_left_thumb = current_position[-1]
                            distance = l_distance
                            answer.extend("L")
                            print("answer", answer, " '5' ")
                            print("DISTANCE:", distance, "\n")
                        else:
                            current_right_thumb = current_position[-1]
                            distance = r_distance
                            answer.extend("R")
                            print("answer", answer, " '6' ")
                            print("DISTANCE:", distance, "\n")

    answer = "".join(answer)
    print("ANSWER:", answer)
    return answer


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"

solution(numbers, hand)
