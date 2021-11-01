# v1 - 재귀사용
# n, m = map(int, input().split())
# nlist = [i for i in range(1, n+1)]
# temp = []
#
# def nm(start):
#     if len(temp) == m:
#         print(*temp)
#         return
#     for i in range(start, n):
#         if nlist[i] not in temp:
#             temp.append(nlist[i])
#             nm(i+1)
#             temp.pop()
# if m == 1:
#     print(*nlist, sep='\n')
# else:
#     nm(0)


# v2 - 조합 사용(순서 고려 안함)
from itertools import combinations
n, m = map(int, input().split())
nlist = [i for i in range(1, n+1)]

if m == 1:
    print(*nlist, sep='\n')
else:
    for i in list(combinations(nlist, m)):
        print(*i, sep=' ')