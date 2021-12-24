# 9095 1, 2, 3 더하기

n = int(input())
nlist = [int(input()) for _ in range(n)]
result = [0, 1, 2, 4]

nmax = max(nlist)
if nmax > 3:
    for i in range(4, nmax + 1):
        result.append(sum(result[i - 3:i]))

for j in nlist:
    print(result[j])
