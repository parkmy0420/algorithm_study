import sys
from collections import deque
input = sys.stdin.readline
max_x = 100001
visited = [0]*max_x
n, k = map(int, input().split())

q = deque([[n, 0]])
visited[n] = 1
while q:
    if visited[k] == 1:
        for find in reversed(q):
            if find[0] == k:
                print(find[1])
                break
        break
    x, cnt = q.popleft()
    for i in (x-1, x+1, x*2):
        if 0 <= i < max_x and visited[i] == 0:
            q.append([i, cnt+1])
            visited[i] = 1