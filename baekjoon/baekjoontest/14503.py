# 14503 로봇 청소
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())
# lookdir = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북-0,동-1,남-2,서-3
dirleft = [(0, -1), (-1, 0), (0, 1), (1, 0)]    # 바라보는 방향의 왼쪽
dirback = [(1, 0), (0, -1), (-1, 0), (0, 1)]    # 바라보는 방향의 한 칸 후진
graph = [list(map(int, input().split())) for _ in range(n)]     # 0-청소가능, 1-벽, 2-청소했음

graph[r][c], cnt = 2, 1 # (r,c) 청소 표시
x, y = r, c
while True:
    check = 0
    for dcnt in range(4):
        dx, dy = dirleft[d]
        nx, ny = x + dx, y + dy
        if n > nx >= 0 and m > ny >= 0:
            d = (d+3) % 4
            if graph[nx][ny] == 0:  # 왼쪽 방향 청소 가능
                x, y = nx, ny
                graph[nx][ny] = 2   # 청소했음 표시
                cnt += 1
                break
            else: check += 1   # 왼쪽 방향 청소 불가능

    if check == 4:  # 네 방향 모두 청소가 이미 되어있거나 벽
        dx, dy = dirback[d]
        nx, ny = x + dx, y + dy
        if n > nx >= 0 and m > ny >= 0:
            if graph[nx][ny] == 1: break  # 뒤쪽 방향이 벽이라 후진 불가능
            else:    # 뒤쪽 방향 후진 가능
                if graph[nx][ny] == 0:  # 청소 가능
                    graph[nx][ny] = 2
                    cnt += 1
                x, y = nx, ny
        else: break

print(cnt)
