"""
Original Test Question: https://programmers.co.kr/learn/courses/30/lessons/12901

2016.01.01 is Friday.
Then, what is the date of 2016.a.b?

You are going to receive two numbers "a" and "b", which are the day and month of the year, respectively.
With these two numbers, you need to return the date of 2016.a.b.
The date is SUN, MON, TUE, WED, THU, FRI, SAT from Sunday to Saturday, respectively.


Constraints
1. The year 2016 is a leap year.
   * The leap year is also known as an "intercalary year" or "bissextile year".
     It is a calendar year that contains an additional day.

2. The two numbers should be existing days of the year.
   For example, a.b cannot be 13.26 or 2.45.


Example
a	b	result
5	24	"TUE"
"""

# January
# SUN MON TUE WED THU FRI SAT
#                       1   2
#   3   4   5   6   7   8   9
#  10  11  12  13  14  15  16
#  17  18  19  20  21  22  23
#  24  25  26  27  28  29  30
#  31

# February
# SUN MON TUE WED THU FRI SAT
#       1   2   3   4   5   6
#   7   8   9  10  11  12  13
#  14  15  16  17  18  19  20
#  21  22  23  24  25  26  27
#  28  29

# March
# SUN MON TUE WED THU FRI SAT
#           1   2   3   4   5
#   6   7   8   9  10  11  12
#  13  14  15  16  17  18  19
#  20  21  22  23  24  25  26
#  27  28  29  30  31

# When "a" is 1, the remainder of b / 7 is 3 because b is 10.
# In 2016, January 10th is a Sunday.
# It means that 10 is placed in the first column of the calendar.
# So, to return the date of a day, we need to find what column the day is in.

# But first, we need to check the month.
# The number of days in each month is stored in the dictionary, "number_of_days".

# For a certain month, we need to sum up all the number of days from January to the previous month of "a".
# For example, if a is 3, then we need to sum up all the number of days from January first to February 29th,
# and the result is 31 + 29 = 60.
# Then, we need to sum "b" to the result.
# For example, if a = 3 and b = 10, then the result is 60 + 10 = 70.

# By doing this calculation, we can find the column of the day by dividing the result by 7 and finding the remainder.
# In the case above, the result is 70 % 7 = 0, and in 2016, the first day of the year is placed on sixth column.
# So, March 10th will be placed in the first column of the calendar.
# The return we need to return is "THU".


number_of_days = {
    1: '31', 2: '29', 3: '31', 4: '30', 5: '31', 6: '30',
    7: '31', 8: '31', 9: '30', 10: '31', 11: '30', 12: '31'
}

date_list = {
    0: "THU", 1: "FRI", 2: "SAT", 3: "SUN", 4: "MON", 5: "TUE", 6: "WED"
}


def solution(a, b):
    answer = ''

    if a == 1:
        answer = date_list[b % 7]
    else:
        for i in range(1, a):
            b += int(number_of_days[i])
        answer = date_list[b % 7]
    return answer


a = 3
b = 10
print(solution(3, 10))
