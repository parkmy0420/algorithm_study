# import sys
# input = sys.stdin.readline
#
# testcase = int(input())
# for _ in range(testcase):
#     m, n, k = map(int, input().split())
#

#
import sys
from collections import deque
input = sys.stdin.readline

check = [[0]*5 for _ in range(5)]

def bfs(x, y, level, check):
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque([(x, y, level)])
    check[x][y] = 1

    while q:
        x, y, level = map(int, q.popleft())
        if x == 4 and y == 4:
            return level
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 5 and 0 <= ny < 5 and check[nx][ny] == 0:
                check[nx][ny] = 1
                # graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny, level+1))

print(bfs(0,0,0, check))

