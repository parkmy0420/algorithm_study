# 1931_회의실 배정

def roomfind(i, find):
    global cnt
    for j in range(i+1, n):
        if find <= time[j][0]:
            cnt += 1
            roomfind(j, time[j][1])
            break

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time.sort(key=lambda x: (x[1], x[0]))
roomcnts = []
last = time[0][1]

for i in range(n):
    cnt = 1
    if i == 0 or time[i][1] < last:
        last = time[i][1]
        roomfind(i, time[i][1])
        roomcnts.append(cnt)

print(max(roomcnts))