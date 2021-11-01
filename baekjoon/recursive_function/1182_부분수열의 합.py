# s1
# import sys
# input = sys.stdin.readline
# n, s = map(int, input().split())
# nlist = list(map(int, input().split()))
# temp, cnt = [], 0
#
# def dfs(a, num):
#     global cnt
#     if len(temp) == num:
#         if sum(temp) == s:
#             cnt += 1
#         return
#     for j in range(a, n):
#         temp.append(nlist[j])
#         dfs(j+1, num)
#         temp.pop()
#
# for i in range(1, n+1):
#     dfs(0, i)
# print(cnt)


# s2 - 시간 효율 더 좋음
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
nlist = list(map(int, input().split()))
cnt = 0

def dfs(idx, sum):
    global cnt
    if idx >= n:
        return
    sum += nlist[idx]
    if sum == s:
        cnt += 1

    dfs(idx+1, sum - nlist[idx])
    dfs(idx+1, sum)

dfs(0,0)
print(cnt)