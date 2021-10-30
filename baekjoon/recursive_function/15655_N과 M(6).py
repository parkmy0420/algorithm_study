n, m = map(int, input().split())
nlist = sorted(list(map(int,input().split())))
temp = []

def nm():
    if len(temp) == m:
        print(*temp)
        return
    for i in range(n):
        if not temp or temp[-1] < nlist[i]:
            temp.append(nlist[i])
            nm()
            temp.pop()
if m == 1:
    print(*nlist, sep='\n')
else:
    nm()