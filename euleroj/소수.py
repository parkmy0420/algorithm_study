
m, n = int(input()), int(input())

nnum, mnum = set(range(2,n+1)), set(range(2,m))

for i in range(2, int(n ** 0.5)+1):
    if i in nnum:
        nnum -= set(range(2*i, n+1, i))

nnum = nnum - mnum
if len(nnum) == 0:
    print(-1)
else:
    print(sum(nnum))
    print(min(nnum))
