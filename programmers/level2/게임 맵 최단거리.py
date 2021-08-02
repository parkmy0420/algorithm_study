# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

def solution(maps):
    from collections import deque
    udlr = [[1, 0], [-1, 0], [0, -1], [0, 1]]   #상하좌우 이동
    n, m = len(maps), len(maps[0])  # 맵 크기인 n*m 구하기
    queue = deque()
    queue.append([0,0,1]) # 시작점 & cnt 1 입력

    while queue:
        y, x, cnt = queue.popleft()
        maps[y][x] = 0

        for i in range(len(udlr)):
            dy = y + udlr[i][0]
            dx = x + udlr[i][1]

            # 다음 위치로 이동했을 때 목적지인 경우
            if dy == n-1 and dx == m-1:
                return cnt + 1

            elif 0 <= dy < n and 0 <= dx < m and maps[dy][dx] == 1:
                maps[dy][dx] = 0    # 다시 돌아 올 수 없게 현재 위치 0
                queue.append((dy, dx, cnt+1))
    return -1

print(solution(maps))