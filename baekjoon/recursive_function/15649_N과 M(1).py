# v1 - 재귀사용
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
    print(*nlist, sep='\n')
else:
    nm(0)

# v2 - 순열 사용(순서 고려)
# from itertools import permutations
# n, m = map(int, input().split())
# nlist = [i for i in range(1, n+1)]
#
# if m == 1:
#     print(*nlist, sep='\n')
# else:
#     for i in list(permutations(nlist, m)):
#         print(*i, sep=' ')
