# name = "JAZ"
name = "JEROEN"
# name = "JAN"
# name = 'ABABAAAAAAABA'
# name = 'ABAABB'
# name = 'BAAABA'


def solution(name):
    answercnt, nowindex, indexcnt, tf = 0, 0, 0, True
    name = list(name)
    while tf:
        l, r = 1, 1
        if name.count('A') == len(name):
            tf = False
        else:
            # 상하 이동하는 파트
            if name[nowindex] != 'A':
                answercnt += min((ord(name[nowindex]) - 65), 91 - ord(name[nowindex]))
                name[nowindex] = 'A'
                continue
            # 좌우 이동하는 파트
            else:
                # 왼쪽
                while name[nowindex - l] == 'A':
                    l += 1
                # 오른쪽
                while name[nowindex + r] == 'A':
                    r += 1

                if l < r:
                        answercnt += l
                        nowindex += -l
                else:
                        answercnt += r
                        nowindex += r

    return answercnt




# 4, 7 테스트 실패한 경우
# def solution(name):
#     answercnt, nowindex, indexcnt, tf = 0, 0, 0, True
#     name = list(name)
#     num = [i for i, x in enumerate(name) if x != 'A']
#     while tf:
#         if name.count('A') == len(name):
#             tf = False
#         else:
#             # 상하 이동하는 파트
#             if name[nowindex] != 'A':
#                 answercnt += min((ord(name[nowindex]) - 65), 91 - ord(name[nowindex]))
#                 name[nowindex] = 'A'
#                 del num[num.index(nowindex)]
#                 continue
#             # 좌우 이동하는 파트
#             else:
#                 if not num:
#                     return answercnt
#                 else:
#                     if abs(num[0] - nowindex) <= abs(len(name) + nowindex - num[-1]):
#                         answercnt += abs(num[0] - nowindex)
#                         nowindex = num[0]
#                     else:
#                         answercnt += abs(len(name) + nowindex - num[-1])
#                         nowindex = num[-1]
#
#     return answercnt
#

print(solution(name))


