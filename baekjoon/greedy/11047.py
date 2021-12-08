# 11047 동전 0

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = 0

for i in reversed(coins):
    if k == 0:
        break
    temp, k = divmod(k, i)
    cnt += temp

print(cnt)
