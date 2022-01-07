# 2839 설탕 배달
n = int(input())
dp = [0] + [5001]*n

for j in [3, 5]:
    for i in range(j, n+1):
        dp[i] = min(dp[i], dp[i-j]+1)

print(dp[n] if dp[n] != 5001 else -1)
