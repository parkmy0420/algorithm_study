# 1080 행렬

def switch(i,j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            a[x][y] = 1 - a[x][y]

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().strip())) for _ in range(n)]
b = [list(map(int, input().strip())) for _ in range(n)]
cnt = 0

if a == b:
    print(0)
elif n >= 3 and m >= 3:
    for i in range(0, n-2):
        for j in range(0, m-2):
            if a[i][j] != b[i][j]:
                cnt += 1
                switch(i,j)
    if a == b:
        print(cnt)
    else:
        print(-1)
else:
    print(-1)