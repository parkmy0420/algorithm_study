# v1 - 재귀사용
# n, m = map(int, input().split())
# nlist = [i for i in range(1, n+1)]
# temp = []
#
# def nm():
#     if len(temp) == m:
#         print(*temp)
#         return
#     for i in range(n):
#         temp.append(nlist[i])
#         nm()
#         temp.pop()
# if m == 1:
#     print(*nlist, sep='\n')
# else:
#     nm()


# v2 - product 사용
from itertools import product
n, m = map(int, input().split())
nlist = [i for i in range(1, n+1)]

if m == 1:
    print(*nlist, sep='\n')
else:
    for i in list(product(nlist, repeat=m)):
        print(*i, sep=' ')