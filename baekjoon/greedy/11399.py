# 11399 ATM

import sys
input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))
times.sort()
result, temp = 0, 0

for i in times:
    temp += i
    result += temp

print(result)