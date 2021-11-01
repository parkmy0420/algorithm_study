import sys
input = sys.stdin.readline
n = int(input())
nlist = list(map(int, input().split()))
summax = 0

def dfs(idx, sum, temp, used):
    global summax
    if idx == n:
        sumtemp = 0
        for i in range(n-1):
            sumtemp += abs(temp[i] - temp[i + 1])
        if summax < sumtemp:
            summax = sumtemp
        return
    for i in range(n):
        if i not in used:
            temp.append(nlist[i])
            used.append(i)
            dfs(idx+1, sum, temp, used)
            temp.pop()
            used.pop()
dfs(0,0,[],[])
print(summax)
