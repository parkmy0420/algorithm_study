# 10162 전자레인지

n = int(input())
time = []

for s in [300, 60, 10]:
    t, n = divmod(n, s)
    time.append(t)

if n == 0: print(*time, sep=' ')
else: print(-1)