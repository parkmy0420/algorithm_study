import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[*map(int, input().strip())] for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]   # 상하좌우 이동변수

queue = [(0, 0)]    # 시작 좌표
visited[0][0] = True     # 시작 좌표 노드 방문 표시

while queue:    # 큐가 빌 때까지
    x, y = queue.pop(0)

    if x == n-1 and y == m-1:   # 마지막 지점에 도착하면 break
        print(graph[x][y])
        break

    for i in range(4):  # 상하좌우 이동-> 4번
        nx = x + dx[i]
        ny = y + dy[i]
        if n > nx >= 0 and m > ny >= 0 and graph[nx][ny] and visited[nx][ny] == False:
            queue.append((nx, ny))
            visited[nx][ny] = True
            graph[nx][ny] += graph[x][y]

