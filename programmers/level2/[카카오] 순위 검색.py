info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

from itertools import combinations as cb
from collections import defaultdict #딕셔너리 만드는 dict클래스의 서브클래스

def solution(info, query):
    info_dict = defaultdict(list)
    answer = []

    for i in info:  # 지원자 정보 파싱
        temp = i.split()
        score_info = int(temp[-1])  # 점수만 찾아내 infopoint에 저장
        key_info = temp[:-1]   # 조건들만 infotemp에 저장

        for j in range(5):
            for c in cb(key_info, j):   #한 지원자의 경우의 수 16개를 만들기
                one_info_key = ''.join(c)
                info_dict[one_info_key].append(score_info)
                # 한 지원자의 info 조건 조합을 key, 점수를 value로 딕셔너리 저장

    for infopoint in info_dict.keys():
        info_dict[infopoint].sort() # value(점수)들을 오름차순 정렬, binary search 위함

    for i in query:
        temp = i.split()
        temp = [k for k in temp if k != 'and']  # and 제거
        scorer_query = int(temp[-1]) # 점수만 찾아내 querypoint 리스트에 저장
        querytemp = temp[:-1]  # 조건들만 querytemp 리스트에 저장
        querytemp = ''.join([k for k in querytemp if k != '-'])  # '-' 제거

        # score_query보다 큰 점수 개수 구하기
        if querytemp in info_dict:
            score = info_dict[querytemp]
            if len(score) > 0:
                l, r = 0, len(score)
                while l < r:
                    m = (l + r) // 2
                    if score[m] >= scorer_query:
                        r = m
                    else:
                        l = m + 1
                answer.append(len(score)-l)
        else:
            answer.append(0)
    return answer
print(solution(info, query))


