# 1912 연속합_220308

n = int(input())
nlist = list(map(int, input().split()))
dplist = [nlist[0]]

for i in range(1, len(nlist)):
    now = nlist[i]
    dplist.append(dplist[i-1]+now if dplist[i-1]+now > now else now)

print(max(dplist))