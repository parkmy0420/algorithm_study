# 1920 수 찾기

def binary(findnum):
    left, right = 0, n-1
    while left <= right:
        mid = (left + right)//2
        check = nlist[mid]
        if check == findnum:
            return True
        elif check < findnum:
            left = mid + 1
        else:
            right = mid - 1

import sys
input = sys.stdin.readline
n = int(input())
nlist = sorted(list(map(int, input().split())))
m = int(input())
mlist = list(map(int, input().split()))

for findnum in mlist:
    print(1 if binary(findnum) else 0)

# # 파이썬 in 사용 ->  list -> 시간 초과, set -> 통과 시간 빠름
# import sys
# input = sys.stdin.readline
# n = int(input())
# nlist = set(map(int, input().split())) # list -> 시간 초과, set -> 통과 시간 빠름
# m = int(input())
# mlist = list(map(int, input().split()))
#
# for findnum in mlist:
#     print(1 if findnum in nlist else 0)