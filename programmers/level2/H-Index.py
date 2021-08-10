# citations = [3, 0, 6, 1, 5]
# citations = [10, 8, 5, 4, 3] #4
# citations = [25, 8, 5, 3, 3] #3
# citations = [0, 0, 0] #0
# citations = [0, 1, 1] #1
# citations = [0, 1, 2] #1
# citations = [11, 9] #2
# citations = [0, 0, 0, 0, 1] #1
# citations = [1, 3, 5, 7, 9, 11] #4
citations = [0,1,2,3,3,3,3,3,3,4,10,20,30,40] #4
# citations = [5, 5, 5, 5]    #4

def solution(citations):
    answer = -1
    citations.sort()

    for i in range(len(citations)):
        if len(citations[i:]) >= citations[i]:
            if citations[i] > answer:
                answer = citations[i]
            if i != len(citations)-1 and citations[i+1]-citations[i] not in (0, 1):
                for j in range(1, citations[i+1]-citations[i]):
                    if len(citations[i+1:]) >= citations[i]+j:
                        if citations[i]+j > answer:
                            answer = citations[i]+j

    if answer == -1:
        answer = len(citations)

    return answer

#
# # 다른 풀이
# def solution(citations):
#     citations.sort()
#     l = len(citations)
#     for i in range(l):
#         if citations[i] >= l-i:
#             return l-i
#     return 0

print(solution(citations))