# 2468 안전영역

def bfs(x, y, water):
    q = deque([[x, y]])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: # 상하좌우
            nx, ny = x + dx, y + dy
            if n > nx >= 0 and n > ny >= 0:
                if nlist[nx][ny] > water and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
nlist, maxpoint, islands = [], 0, [1]

for i in range(n):  # append list
    nlist.append(list(map(int, input().split())))
    maxpoint = max(max(nlist[-1]), maxpoint)  # find max

for water in range(1, maxpoint+1):    # 물 높이 별 섬의 개수
    visited = [[0] * n for _ in range(n)]  # 방문 여부
    island = 0
    for x in range(n):
        for y in range(n):
            if visited[x][y] == 0:
                if nlist[x][y] > water:
                    bfs(x, y, water)
                    island += 1
                else:
                    visited[x][y] = 1
    islands.append(island)
print(max(islands))