# 2747 피보나치 수

n = int(input())
fibo = [0]*(n+1)

for i in range(1, n+1):
    if i == 1:
        fibo[1] = 1
    else:
        fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[n])