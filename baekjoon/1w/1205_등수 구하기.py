n, newp, p = map(int, input().split())
if n != 0:
    rank = list(map(int, input().split()))
else:
    rank = []

cnt = rank.count(newp)
rank.append(newp)
rank.sort(reverse=True)

if rank.index(newp)+cnt > p-1:
    print(-1)
else:
    print(rank.index(newp)+1)

