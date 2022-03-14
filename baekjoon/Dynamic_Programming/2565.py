# 2565 전깃줄
import sys
input = sys.stdin.readline
n = int(input())
nums = sorted([list(map(int, input().split())) for _ in range(n)])
dp = [1]*n

for i in range(1, n):  # 비교하는 주체
    for j in range(i):  # 비교당하는 대상
        if nums[i][1] > nums[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))