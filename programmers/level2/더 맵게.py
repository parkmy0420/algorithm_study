scoville, K =[1, 2, 3, 9, 10, 12], 7
# scoville, K =[1, 1, 1, 1], 11

# sorted 사용한 방법
# def solution(scoville, K):
#     answer, cnt = 0, 0
#     while min(scoville) <= K:
#         if len(scoville) == 1:
#             return -1
#         else:
#             scoville = sorted(scoville)
#             answer = scoville[0]+scoville[1]*2
#             del scoville[0:2]
#             scoville.append(answer)
#             cnt += 1
#
#     return cnt

# min 사용한 방법
# def solution(scoville, K):
#     answer, cnt = 0, 0
#     while min(scoville) <= K:
#         if len(scoville) == 1:
#             return -1
#         else:
#             answer = scoville.pop(scoville.index(min(scoville)))+scoville.pop(scoville.index(min(scoville)))*2
#             scoville.append(answer)
#             cnt += 1
#
#     return cnt

def solution(scoville, K):
    import heapq
    cnt = 0
    heapq.heapify(scoville)
    while scoville[0] <= K:
        if len(scoville) == 1:
            return -1
        else:
            heapq.heappush(scoville, (heapq.heappop(scoville)+heapq.heappop(scoville)*2))
            cnt += 1
    return cnt

print(solution(scoville, K))