def bfs(info):
    size = info[0][0]
    s1, s2 = info[1][0], info[1][1]
    graph = [[0]*size for _ in range(size)]
    queue = [(s1, s2)]    # 시작 좌표

    while queue:    # 큐가 빌 때까지
        x, y = queue.pop(0)
        if x == info[2][0] and y == info[2][1]:   # 목표 지점에 도착하면 break
            print(graph[x][y])
            break
        for i in range(8):  # 8방향 이동
            nx = x + dx[i]
            ny = y + dy[i]
            if size > nx >= 0 and size > ny >= 0 and graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] += (graph[x][y] + 1)

import sys
input = sys.stdin.readline
num = int(input())
dx, dy = [-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]   # 8방향 이동좌표

for i in range(num):
    info = []
    for j in range(3):
        info.append(list(map(int, input().split())))
    bfs(info)