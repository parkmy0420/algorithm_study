# 1149 RGB거리

import sys
input = sys.stdin.readline
n = int(input())
houses = [list(map(int, input().split())) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + houses[i - 1][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + houses[i - 1][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + houses[i - 1][2]

print(min(dp[n]))
