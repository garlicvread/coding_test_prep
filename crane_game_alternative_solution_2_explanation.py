"""
# The Code to Explain:

cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
a, s = 0, [0]

for m in moves:
    if len(cols[m - 1]) > 0:
        if (d := cols[m - 1].pop(0)) == (l := s.pop()):
            a += 2
        else:
            s.extend([l, d])
"""


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print("\n")

print("The type of \"zip(*board))\": ", type(zip(*board)), "\n")

t_board = list(zip(*board))
print("t_board: ", t_board)

"""
Original Matrix
[[0, 0, 0, 0, 0],
 [0, 0, 1, 0, 3],
 [0, 2, 5, 0, 1],
 [4, 2, 4, 4, 2],
 [3, 5, 1, 3, 1]]

The outcome of list(zip(*board)): Transposed Matrix of the Original Matrix
[(0, 0, 0, 4, 3),
 (0, 0, 2, 2, 5),
 (0, 1, 5, 4, 1),
 (0, 0, 0, 4, 3),
 (0, 3, 1, 2, 1)]
"""

print("-----------------------------------------------------")
lambda_x = lambda x: list(filter(lambda y: y > 0, x))
print("t_board[0]: ", t_board[0], "\n")
print("lambda_x(t_board[0]): ", lambda_x(t_board[0]))

"""
lambda y: y > 0 --> for each element in the list,
                    if the element is greater than 0 return True,
                    else return False.

filter(lambda y: y > 0, x) --> filter the elements in x that are greater than 0.

    filter(a, b) function:
        a: function that works as condition
        b: iterable data
        
Thus "lambda x" contains the list of the elements that are greater than zero in each column of the transposed matrix. 
"""

print("-----------------------------------------------------")
cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
print("cols: ", cols, "\n")
print("len(cols): ", len(cols))

"""
Let's look how the lambda function and the filter function work together.
lambda_x(t_board[0]) receives t_board[0] as its argument.
t_board[0] is a list of the first row of the transposed matrix.
The lambda function will filter the elements in t_board[0] that are greater than 0.


Using map() function, we can map the lambda function to each element in the transposed matrix. 


    map(a, b) function:
        a: The function to apply.
        b: The objects to apply the function to.
    
    
    1. The object must be iterable: list, tuple, string, set, dictionary, generator, etc.
    2. The return of map() is a map object, thus you need to convert it to a list or tuple. 
    
    map() function inputs each element of the iterable object (the second parameter)
    and return a list of the result of the function (the first parameter).
    
    Let's assume that the first parameter is a function that add 1 to each element of the iterable object.
    When the second parameter is [1, 2, 3, 4, 5], the return of map() is [2, 3, 4, 5, 6].


    Let's look how it actually works.
    Let's assume that the function we have is:
    
    def function_to_apply(x):
        return x + 1
        
        
    and also assume that the object we have is:
    
    object_to_map = [1, 2, 3, 4, 5]
    
    
    If we map those two things together, the return of map() is:
    
    print(list(map(function_to_apply, object_to_map)))
        --> return: [2, 3, 4, 5, 6]
"""

# a: the number of erased numbers.
# s: the stack of numbers.
#    The reason why you assign [0] to s is because if you do not assign [0] to s,
#    then you will get an error when you try to pop() from an empty list.
print("-----------------------------------------------------")
a, s = 0, [0]
print("a: ", a, ", s: ", s, "\n")

"""
Now is the time to look into the code:

# for m in moves:
#     if len(cols[m - 1]) > 0:
#         if (d := cols[m - 1].pop(0)) == (l := s.pop()):
#             a += 2
#         else:
#             s.extend([l, d])


You can use ":=" to assign a value to a variable, but let's see how the traditional code works first.

For ":=" operator, you can use following webpages.
1. https://nanarin.tistory.com/287
2. https://www.python.org/dev/peps/pep-0572/

For "extend()" function, you can use following webpages.
1. https://ooyoung.tistory.com/117
"""

for m in moves:
    print("m - the column you are at: ", m)
    print("len(cols[m-1]) - the number of remaining numbers at that column: ", len(cols[m-1]))

    # Thus:
    if len(cols[m-1]) > 0:
        if cols[m-1][0] == s[-1]:
            print("cols[m-1][0] - the number you picked up: ", cols[m-1][0])
            a += 2
            s.pop()
            print("s:", s, "\n")
        else:
            s.append(cols[m-1].pop(0))
            print("s:", s, "\n")

print("------------------------------------------------------")
print("a - the number of erased numbers: ", a)
print("s - the final stack: ", s)
print("s[1:]:", s[1:], "\n")


"""
The whole outcome of this code is:




The type of "zip(*board))":  <class 'zip'> 

t_board:  [(0, 0, 0, 4, 3), (0, 0, 2, 2, 5), (0, 1, 5, 4, 1), (0, 0, 0, 4, 3), (0, 3, 1, 2, 1)]
-----------------------------------------------------
t_board[0]:  (0, 0, 0, 4, 3) 

lambda_x(t_board[0]):  [4, 3]
-----------------------------------------------------
cols:  [[4, 3], [2, 2, 5], [1, 5, 4, 1], [4, 3], [3, 1, 2, 1]] 

len(cols):  5
-----------------------------------------------------
a:  0 , s:  [0] 

m - the column you are at:  1
len(cols[m-1]) - the number of remaining numbers at that column:  2
s: [0, 4] 

m - the column you are at:  5
len(cols[m-1]) - the number of remaining numbers at that column:  4
s: [0, 4, 3] 

m - the column you are at:  3
len(cols[m-1]) - the number of remaining numbers at that column:  4
s: [0, 4, 3, 1] 

m - the column you are at:  5
len(cols[m-1]) - the number of remaining numbers at that column:  3
cols[m-1][0] - the number you picked up:  1
s: [0, 4, 3] 

m - the column you are at:  1
len(cols[m-1]) - the number of remaining numbers at that column:  1
cols[m-1][0] - the number you picked up:  3
s: [0, 4] 

m - the column you are at:  2
len(cols[m-1]) - the number of remaining numbers at that column:  3
s: [0, 4, 2] 

m - the column you are at:  1
len(cols[m-1]) - the number of remaining numbers at that column:  1
s: [0, 4, 2, 3] 

m - the column you are at:  4
len(cols[m-1]) - the number of remaining numbers at that column:  2
s: [0, 4, 2, 3, 4] 

------------------------------------------------------
a - the number of erased numbers:  4
s - the final stack:  [0, 4, 2, 3, 4]
s[1:]: [4, 2, 3, 4] 


Process finished with exit code 0
"""
