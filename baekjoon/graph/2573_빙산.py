def bfs():
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append(iceberg[0])    # 시작 좌표
    visited[q[0][0]][q[0][1]] = 1  # 시작 좌표 노드 방문 표시
    cnt = 0     # 이어진 빙산의 개수

    while q:  # 큐가 빌 때까지
        x, y = q.popleft()
        cnt += 1
        zerocnt = 0  # 상하좌우에 0이 저장된 칸의 개수
        for i in range(4):  # 상하좌우 이동-> 4번
            nx, ny = x + dx[i], y + dy[i]
            if n > nx >= 0 and m > ny >= 0:
                if graph[nx][ny] > 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                if graph[nx][ny] <= 0:
                    zerocnt += 1
        if zerocnt != 0:
            meltinfo.append((x, y, zerocnt))
    while meltinfo:  # 빙산 높이 변경
        i1, i2, i3 = meltinfo.popleft()
        graph[i1][i2] -= i3
        if graph[i1][i2] <= 0 and (i1, i2) in iceberg:
            iceberg.remove((i1, i2))
    return cnt

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우 이동변수
graph = [[*map(int, input().split())] for _ in range(n)]
result = 0  # result: 빙산이 분리되는 최초의 시간
meltinfo = deque([])  # 빙산 녹는 위치, 정도 정보 저장
iceberg = []   # 빙산

for i in range(1, n-1):
    for j in range(1, m-1):
        if graph[i][j] != 0:
            iceberg.append((i, j))

while True:
    if len(iceberg) != bfs():   # 전체 빙산 개수와 시작 빙산과 이어져있는 빙산 개수 비교
        print(result)   # 두 덩어리 이상인 경우 출력
        break
    result += 1

    if sum(map(sum, graph[1:-1])) == 0:
        print(0)
        break