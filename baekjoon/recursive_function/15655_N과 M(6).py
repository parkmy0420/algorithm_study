n, m = map(int, input().split())
nlist = sorted(list(map(int,input().split())))
temp = []

def nm(start):
    if len(temp) == m:
        print(*temp)
        return
    for i in range(start, n):
        temp.append(nlist[i])
        nm(i+1)
        temp.pop()
if m == 1:
    print(*nlist, sep='\n')
else:
    nm(0)


# import sys
# from itertools import combinations
# input = sys.stdin.readline
# n, m = map(int, input().split())
# nlist = sorted(list(map(int,input().split())))
#
# if m == 1:
#     print(*nlist, sep='\n')
# else:
#     for i in list(combinations(nlist, m)):
#         print(*i, sep=' ')