# 12865 평범한 배낭
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
nlist = [list(map(int, input().split())) for _ in range(n)]
check = [0] * (k + 1)

for i in range(n):
    w, v = nlist[i]
    for j in range(k, w-1, -1):
        check[j] = max(check[j], check[j-w]+v)
print(check[-1])
