# 2206 벽 부수고 이동하기

def bfs():
    q = deque()  # 시작 좌표
    q.append((0, 0, 0, 1))
    check[0][0][0] = 1  # 시작 좌표 노드 방문 표시
    cnt = 0

    while q:  # 큐가 빌 때까지
        x, y, bcnt, result = q.popleft()
        if x == n - 1 and y == m - 1:  # 마지막 지점에 도착하면 break
            cnt += 1
            print(result)
            break

        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if check[nx][ny][0] == 0 or check[nx][ny][1] > bcnt:
                    if graph[nx][ny] == 0:  # 길이 있는 경우
                        check[nx][ny] = [1, bcnt]
                        q.append((nx, ny, bcnt, result+1))
                    elif bcnt == 0:     # 길은 없지만 한번도 벽을 부순적 없는 경우
                        check[nx][ny] = [1, bcnt+1]
                        q.append((nx, ny, bcnt+1, result+1))

    if cnt == 0:    # 벽을 한번 부숴는데 더 이상 길이 없는 경우
        print(-1)

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
relist = []

check = [[[0, 0] for _ in range(m)] for _ in range(n)]  # [방문여부, 벽을 부쉈는지 여부]
bfs()
