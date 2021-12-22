# 1463 1로 만들기

n = int(input())
case, cnt = [-1]*n+[0], 0
from collections import deque
q = deque([n])

while case[1] == -1:
    cnt += 1
    for _ in range(len(q)):
        now = q.popleft()
        if now % 3 == 0 and case[now//3] == -1:
            case[now // 3] = cnt
            q.append(now//3)
        if now % 2 == 0 and case[now // 2] == -1:
            case[now // 2] = cnt
            q.append(now//2)
        if case[now-1] == -1:
            case[now-1] = cnt
            q.append(now-1)

print(case[1])