n, m = map(int, input().split())
nlist = [i for i in range(1, n+1)]
temp = []

def nm(start):
    if len(temp) == m:
        print(*temp)
        return
    for i in range(start, n):
        if nlist[i] not in temp:
            temp.append(nlist[i])
            nm(i+1)
            temp.pop()
if m == 1:
    print(*nlist, sep='\n')
else:
    nm(0)