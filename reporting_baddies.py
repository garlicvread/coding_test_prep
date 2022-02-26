"""
Original test question: https://programmers.co.kr/learn/courses/30/lessons/92334

A user can report other baddies.
There is no limitation of reporting.
However, the report on the same baddie counts as 1.

A user who is reported more than k times will be banned,
and the ban notification will be sent via e-mails to every users who report the banned user.
The e-mail notification will be sent at the same time as the ban.


Example input 1:
["muzi", "frodo", "apeach", "neo"] #id_list
["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]  #report: [id, reported id]
2  #k

Example output 1:
[2,1,1,0]


Example input 2:
["con", "ryan"]  #id_list
["ryan con", "ryan con", "ryan con", "ryan con"]  #report: [id, reported id]
3  #k

Example output 2:
[0,0]
"""

# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
# k = 2


def solution(id_list, report, k):
    """
    param id_list: list of the users.
    param report: list of the reported baddies.
    param k: the number a user can be reported.
    return: the list of the number of e-mail notification each user receive.
    """

    # The banned IDs: report[i][1].
    reported_id = [report.split()[1] for report in set(report)]
    # print(reported_id)

    ids_to_be_banned = [id for id in set(id_list) if reported_id.count(id) >= k]
    # print(ids_to_be_banned)

    users_who_notified = [bans.split()[0] for bans in set(report) if bans.split()[1] in ids_to_be_banned]
    # print(users_who_notified)

    result = [users_who_notified.count(i) for i in id_list]
    # print(result)

    return result
