# 13458 시험 감독
import sys
input = sys.stdin.readline
n = int(input())
testnums = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0

for i in testnums:
    answer += 1
    temp = (i-b) // c
    if (i-b) <= 0: continue
    elif (i-b) % c == 0: answer += temp
    else: answer += (temp + 1)

print(answer)