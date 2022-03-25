# 1978 소수 찾기

n = int(input())
nlist = list(map(int, input().split()))
nmax, cnt = max(nlist), 0
check = [0] * (nmax+1)

for i in range(2, int(nmax**0.5)+1):
    for j in range(2*i, nmax+1, i):
        check[j] = 1

for k in nlist:
    if k not in [0, 1] and check[k] == 0:
        cnt += 1

print(cnt)