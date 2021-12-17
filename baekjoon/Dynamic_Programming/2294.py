# 2294 동전 2

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
case = [0]+[10001]*k

for coin in coins:
    for i in range(coin, k+1):
        case[i] = min(case[i], case[i-coin]+1)

print(-1 if case[k] == 10001 else case[k])
