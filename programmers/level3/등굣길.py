import sys
from collections import deque
input = sys.stdin.readline

def solution(m, n, puddles):

    dxy = [(1, 0), (0, 1)]
    q = deque([(0, 0)])  # x, y
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = 1
    ans = 0
    while q:
        x, y = map(int, q.popleft())
        if x == (n - 1) and y == (m - 1):
            ans = (dp[x-1][y] + dp[x][y-1])% 1000000007
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:     # index 밖
                if [ny+1, nx+1] not in puddles:  # 장애물
                    if dp[nx][ny] == 0:
                        q.append((nx, ny))
                    if nx - 1 < 0:
                        dp[nx][ny] = dp[nx][ny-1]
                    elif ny - 1 < 0:
                        dp[nx][ny] = dp[nx - 1][ny]
                    else:
                        dp[nx][ny] = dp[nx-1][ny] + dp[nx][ny-1]
    return ans


# import sys
# input = sys.stdin.readline
#
# def solution(m, n, puddles):
#     dp = [[0]*(m+1) for _ in range(n+1)]
#     ans = 0
#
#     for nx, ny in puddles:
#         dp[nx][ny] = -1
#     for x in range(1, n+1):
#         for y in range(1, m+1):
#             if x == n and y == m:
#                 ans = (dp[x-1][y] + dp[x][y-1]) % 1000000007
#             if [y, x] not in puddles:  # 장애물
#                 pl = dp[x-1][y] + dp[x][y-1]
#                 if pl == 0:
#                     dp[x][y] = 1
#                 else:
#                     dp[x][y] = pl
#     return ans
print(solution(5, 4, [[2, 2],[2, 4], [3, 2]]))