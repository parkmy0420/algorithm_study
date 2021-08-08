import math
n = int(input())
nlist = [int(input()) for _ in range(n)]

for j in range(n):
    if str(nlist[j])[-2] == '5':
        print(int((nlist[j]+50) / 100) * 100)
    else:
        print(round(nlist[j], -2), end=' ')
    print(int(nlist[j] / 100) * 100)