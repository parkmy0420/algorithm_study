def bfs(x, y):
    dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]  # 상하좌우대각선 이동변수

    queue = [(x, y)]  # 시작 좌표
    visited[x][y] = True  # 시작 좌표 노드 방문 표시

    while queue:  # 큐가 빌 때까지
        x, y = queue.pop(0)
        global w
        global h

        for i in range(8):  # 상하좌우대각선 이동-> 8번
            nx = x + dx[i]
            ny = y + dy[i]
            if h > nx >= 0 and w > ny >= 0 and visited[nx][ny] == False:
                visited[nx][ny] = True
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] += graph[x][y]

import sys
input = sys.stdin.readline

while True:     #테스트 케이스가 끝날 때 까지 반복
    w, h = map(int, input().split())
    if w == h == 0:     # 0 0이 입력되면 종료
        break
    cnt = 0
    visited = [[False]*w for _ in range(h)]
    graph = [list(map(int, input.split())) for _ in range(h)]

    for j in range(h):
        while False in visited[j]:  # 방문하지 않은 노드가 없을때까지 반복
            tempy = visited[j].index(False)
            if graph[j][tempy] == 1:
                cnt += 1
                bfs(j, tempy)
            else:
                visited[j][tempy] = True
    print(cnt)