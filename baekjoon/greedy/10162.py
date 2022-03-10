# 10162 전자레인지

n = int(input())
time = []

for s in [300, 60, 10]:
    t, n = divmod(n, s)
    time.append(t)

for i in time:
    if n == 0: print(i, end=' ')
    else:
        print(-1)
        break