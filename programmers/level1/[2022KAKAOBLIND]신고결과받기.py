# def solution(id_list, report, k):
#     id_num = len(id_list)
#     report_time = [0] * id_num
#     user_report_list = [[] for _ in range(id_num)]
#     sent = []
#
#     for i in report:    # 신고한 사람, 신고된 사람 정리
#         a, b = i.split()
#         n = id_list.index(a)
#         if b not in user_report_list[n]:
#             user_report_list[n].append(b)
#             report_time[id_list.index(b)] += 1
#
#     for j in range(id_num):     # 정지된 유저 저장
#         if report_time[j] >= k:
#             sent.append(id_list[j])
#
#     report_time = [0] * id_num  # 초기화
#     for k in range(id_num):     # 유저가 정지시킨 사람 수
#         for stop_u in sent:
#             if stop_u in user_report_list[k]:
#                 report_time[k] += 1
#
#     return report_time

def solution(id_list, report, k):
    id_num = len(id_list)
    report_time = [0] * id_num
    user_report_list = [[] for _ in range(id_num)]
    sent = []

    for i in report:    # 신고한 사람, 신고된 사람 정리
        a, b = i.split()
        n = id_list.index(a)
        if b not in user_report_list[n]:
            user_report_list[n].append(b)
            report_time[id_list.index(b)] += 1

    for j in range(id_num):     # 정지된 유저 저장
        if report_time[j] >= k:
            sent.append(id_list[j])

    report_time = [0] * id_num  # 초기화
    for l in range(id_num):     # 유저가 정지시킨 사람 수
        for stop_u in sent:
            if stop_u in user_report_list[l]:
                report_time[l] += 1

    return report_time

# print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","muzi apeach","neo apeach","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
# print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))
print(solution(['a','b','c','d','e','f'], ['a b', 'b c', 'a c', 'b d', 'b e', 'b d', 'e f', 'c e'], 2))