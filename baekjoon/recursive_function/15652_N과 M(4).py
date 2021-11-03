n, m = map(int, input().split())
nlist = [i for i in range(1, n+1)]
temp = []

def nm(start):
    if len(temp) == m:
        print(*temp)
        return
    for i in range(start, n):
        temp.append(nlist[i])
        nm(i)
        temp.pop()

if m == 1:
    print(*nlist, sep='\n')
else:
    nm(0)

# v2 - product 사용 -> 메모리초과
# from itertools import product
# n, m = map(int, input().split())
# nlist = [i for i in range(1, n+1)]
#
# if m == 1:
#     print(*nlist, sep='\n')
# else:
#     for i in list(product(nlist, repeat=m)):
#         if list(i) == sorted(i):
#             print(*i, sep=' ')