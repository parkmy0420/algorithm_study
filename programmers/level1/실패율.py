# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 4
stages = [1,1,1,1,2]

def solution(N, stages):
    answer = [0]*N
    num = len(stages)
    a = dict()

    for i in range(1,N+1):
        if num != 0:
            a[i] = stages.count(i) / num
            num = num - stages.count(i)
        else:
            a[i] = 0.0

    for i in range(0,N):
        answer[i] = max(a, key=a.get)
        a.pop(max(a, key=a.get))
    return answer

print(solution(N,stages))