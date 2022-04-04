def solution(id_list, report, k):
    id_num = len(id_list)
    report_time = [0] * id_num  # index user가 신고받은 횟수 저장
    user_report_list = [[] for _ in range(id_num)]
    sent = []   # stop user list
    report = list(set(report))

    for i in report:    # 신고한 사람, 신고된 사람 정리
        a, b = i.split()
        b_index = id_list.index(b)  # reported index
        user_report_list[id_list.index(a)].append(b)    # reporter list
        if report_time[b_index] == k-1:   # stop user append
            sent.append(id_list[b_index])
        else: report_time[b_index] += 1


    report_time = [0] * id_num  # # index user가 신고한 사람 중 정지당한 유저 수

    for j in range(id_num):     # 유저가 정지시킨 사람 수
        ucnt = len(set(user_report_list[j]) & set(sent))
        report_time[j] = ucnt

    return report_time

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
# print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))
# print(solution(['a','b','c','d','e','f'], ['a b', 'b c', 'a c', 'b d', 'b e', 'b d', 'e f', 'c e'], 2))
