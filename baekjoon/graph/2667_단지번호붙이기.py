import sys
input = sys.stdin.readline
n = int(input())
graph = [[*map(int, input().strip())] for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]   # 상하좌우 이동변수
house = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            house.append(1)
            queue = [(i, j)]    # 시작 좌표
            visited[i][j] = True
            while queue:    # 큐가 빌 때까지
                x, y = queue.pop(0)
                for k in range(4):  # 상하좌우 이동-> 4번
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if n > nx >= 0 and n > ny >= 0 and graph[nx][ny] and visited[nx][ny] == False:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        house[-1] += 1

print(len(house))
print(*sorted(house), sep='\n')