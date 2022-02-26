"""
Original Test Question: https://programmers.co.kr/learn/courses/30/lessons/72410

Receiving an ID input, then recommend a similar ID to the user.

ID Creation Rules:
- 3 <= The length of ID <= 15.
- An ID consists of lower case letters, numbers, "-", "_", "." only.
- The period "." cannot be used at the first or last position.


If a new user inputs his ID as "new_id", then the following rules will be applied in order.
    1. Every upper case letter will be transformed into lower case letters.
    2. Erase every character except lower case letters, numbers, "-", "_", ".".
    3. When there are more than two periods in a row, such as "..", replace it as a single period.
    4. If a period is placed at the first or last position, delete it.
    5. If the new_id is a blank string, insert "a" in it.
    6. If the length of the new_id is more than 15, remove all the characters from the 16th character.
       If the result ends with a period, remove the period.
    7. If the length of the new_id is less than 3, input the last character repeatedly until the length becomes 3.


With these rules, when the new_id inputted was "...!@BaT#*..y.abcdefghijklm",
the new_id will be transformed as follows.


1. Upper cases B, T --> lower cases b, t
   ...!@BaT#*..y.abcdefghijklm → ...!@bat#*..y.abcdefghijklm

2. Delete characters that are now allowed. In this case, "!", "@", "#", "*" are deleted.
   ...!@bat#*..y.abcdefghijklm → ...bat..y.abcdefghijklm

3. "..." and ".." are changed into ".".
   ...bat..y.abcdefghijklm → .bat.y.abcdefghijklm

4. The period at the first position is deleted.
   .bat.y.abcdefghijklm → bat.y.abcdefghijklm

5. The new_id is not a blank string, so there is no change.
   bat.y.abcdefghijklm → bat.y.abcdefghijklm

6. The length of new_id is more than 15, so the new_id is truncated to 15 characters.
   bat.y.abcdefghijklm → bat.y.abcdefghi

7. The length of new_id is not less than 3, so there is no change.
   bat.y.abcdefghi → bat.y.abcdefghi


With this process, when a new_id "...!@BaT#*..y.abcdefghijklm" is inputted, it turns into "bat.y.abcdefghi".


Conditions:
- 1 <= The length of new_id <= 1000 and the new_id is a string.
- new_id consists of upper case letters, lower case letters, numbers, and special characters.
- The special characters in new_id is limited into "-_.~!@#$%^&*()=+[{]}:?,<>/".


Examples:
no	new_id                      	result
1.	"...!@BaT#*..y.abcdefghijklm"	"bat.y.abcdefghi"
2.	"z-+.^."	                    "z--"
3.	"=.="	                        "aaa"
4.	"123_.def"	                    "123_.def"
5.	"abcdefghijklmn.p"	            "abcdefghijklmn"


For the second case:
1. No changes.
2. "z-+.^." → "z-.."
3. "z-.." → "z-."
4. "z-." → "z-"
5. No changes.
6. No changes.
7. "z-" → "z--"


For the third case:
1. No changes.
2. "=.=" → "."
3. No changes.
4. "." → "" (new_id becomes a blank string.)
5. "" → "a"
6. No changes.
7. "a" → "aaa"


For the fourth case:
There is no change because the new_id satisfies the conditions.


For the fifth case:
1. No changes.
2. No changes.
3. No changes.
4. No changes.
5. No changes.
6. abcdefghijklmn.p → abcdefghijklmn. → abcdefghijklmn
7. No changes.
"""

import re

characters_to_be_removed = "~!@#$%^&*()=+[{]}:?,<>/"


def solution(new_id):
    # Change the upper cases to lower cases.
    new_id = new_id.lower()

    # Remove all the characters that are not lower case letters, numbers, "-", or ".".
    for characters in characters_to_be_removed:
        if new_id.find(characters) != -1:
            new_id = new_id.replace(characters, "")

    # If there are multiple "."s in a row, replace them with a single ".".
    new_id = re.sub(r'\.+', '.', new_id)

    # Remove the period at the first position.
    if new_id[0] == ".":
        new_id = new_id[1:]

    # If the new_id is a blank string, insert "a" in it.
    if new_id == "":
        new_id = "a"

    # If the length of the new_id is more than 15, remove all the characters from the 16th character.
    # If the result ends with a period, remove the period.
    if len(new_id) > 15:
        new_id = new_id[:15]

    if new_id[-1] == ".":
        new_id = new_id[:-1]

    # If the length of the new_id is less than 3, input the last character repeatedly until the length becomes 3.
    if len(new_id) < 3:
        while len(new_id) < 3:
            new_id = new_id + new_id[-1]

    return new_id


new_id = "z-+.^."

solution(new_id)
