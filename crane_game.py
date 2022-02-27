"""
Original Test Question: https://programmers.co.kr/learn/courses/30/lessons/64061

Let's assume that you are playing a TETRIS-like game.

You have an N * N size squarish 2 dimensional grid.
The whole grid consists of 1 * 1 size grids.

Inside each grid, you may have a number that is stacked from the bottom.
It is also possible that you may not have any number in there.
In this case, the empty grid will be filled with zero(0), and 0 means that the grid is empty.

You also have a storage where you can store the numbers you picked up from the game board.
The size of the storage is big enough to store every number from the game board.

For example, if your game board is 5 * 5 size, it may look like the following.

    Game Board              Storage
    0   0   0   0   0       0
    0   0   1   0   2       0
    0   3   4   0   1       0
    5   3   5   5   3       0
    2   4   1   2   1       0
    -------------------------------
    1   2   3   4   5

The numbers are stacked from the bottom.
It means the numbers are stacked with LIFO(Last In First Out) way.

When you pick up a number from a column, the selected number is deleted from the original location,
and it will be stacked to the storage from the bottom.

While you stack numbers if the same numbers are stacked consecutively,
those two numbers will be deleted.

When you try to pick up a number if there is no number, nothing happens.
This is natural because there is no number placed in an empty grid.


If you pick up numbers from column 1, 5, 3, the game board may look like the following.

    Game Board              Storage
    0   0   0   0   0       0
    0   0   0   0   0       0
    0   3   4   0   1       1
    0   3   5   5   3       2
    2   4   1   2   1       5
    -------------------------------
    1   2   3   4   5


If you pick up a number from column 5, the game board will be changed like the following.

    Game Board              Storage ==> Storage
    0   0   0   0   0       0           0
    0   0   0   0   0       1           0
    0   3   4   0   0       1           0
    0   3   5   5   3       2           2
    2   4   1   2   1       5           5
    -------------------------------
    1   2   3   4   5

Number 1s were stacked in a consecutive way, thus the two 1s were erased.


Parameters
- board: The grid status information. It is a 2 dimensional array, and it contains the number in each grid.
- move: The column where you pick up a number.
- return: The number of numbers that were deleted until the game is over.


Constraints:
- 5 * 5 <= The size of the "board" array <= 30 * 30
- 0 <= The elements of "board" array <= 100: all elements are integers.
- 0 in "board" array means the grid is empty.
- 1 <= The size of "moves" array <= 1000
- 1 <= The elements of "moves" array <= The size of the "board" array


Example input
board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

Example output
result = 4
"""


def store_to_storage(board, moves):
    """
    :param board: The grid status information.
    :param moves: The column where you pick up a number.
    :return: list of numbers you pick up from the game board.
    """
    storage = []

    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i] - 1] == 0:
                continue
            else:
                storage.append(board[j][moves[i] - 1])
                board[j][moves[i] - 1] = 0
                break

    print("The numbers you have picked up: ", storage)
    return storage


def delete_duplicates(list):
    """
    :param list: the inpuit you need to delete the duplicates.
    :return: the number of deleted elements.
    """
    temp = []
    count = 0

    for i in range(len(list)):
        if len(temp) == 0:
            temp.append(list[i])
        else:
            if list[i] == temp[-1]:
                count += 1
                temp.pop()
            else:
                temp.append(list[i])

    answer = count * 2
    print("List after deleting duplication: ", temp)
    print("Number of deleted numbers(answer): ", answer)
    return answer


def solution(board, moves):
    storage = store_to_storage(board, moves)
    answer = delete_duplicates(storage)
    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

solution(board, moves)


"""
# Alternative Solution 1

def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    return answer



# Alternative Solution 2

def solution(board, moves):
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    a, s = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):
                a += 2
            else:
                s.extend([l, d])

    return a    
"""
