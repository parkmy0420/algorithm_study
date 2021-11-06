n, m = map(int, input().split())
nlist = sorted(list(map(int,input().split())))
temp = []

def nm():
    if len(temp) == m:
        print(*temp)
        return
    for i in range(n):
        if nlist[i] not in temp:
            temp.append(nlist[i])
            nm()
            temp.pop()
if m == 1:
    print(*nlist, sep='\n')
else:
    nm()

# import sys
# from itertools import permutations
# input = sys.stdin.readline
# n, m = map(int, input().split())
# nlist = sorted(list(map(int,input().split())))
#
# if m == 1:
#     print(*nlist, sep='\n')
# else:
#     for i in list(permutations(nlist, m)):
#         print(*i, sep=' ')