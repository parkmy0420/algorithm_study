# 2579 계단 오르기

import sys
input = sys.stdin.readline
n = int(input())
stairs = [int(input()) for _ in range(n)]

if n == 1:
    print(stairs[0])
else:
    points = [stairs[0], stairs[0] + stairs[1]] + [0] * (n - 2)  # 각 계단의 점수의 최댓값 저장
    for i in range(2, n):
        points[i] = max(points[i-3]+stairs[i-1]+stairs[i], points[i-2]+stairs[i])
    print(points[-1])