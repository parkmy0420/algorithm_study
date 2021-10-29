n, m = map(int, input().split())
nlist = [i for i in range(1, n+1)]
check = [False]*n   # 중복 check
temp = []

def nm(cnt):
    if cnt == m:
        print(*temp)
        return
    for i in range(n):
        if check[i] == True:
            continue
        temp.append(nlist[i])
        check[i] = True
        nm(cnt+1)
        temp.pop()
        check[i] = False


if m == 1:
    print(*nlist)
else:
    nm(0)

