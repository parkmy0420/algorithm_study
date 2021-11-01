import sys
input = sys.stdin.readline
n = int(input())
nlist = list(map(int, input().split())) # 입력된 숫자 저장
add, sub, mul, div = map(int, input().split())  # 연산자 개수 저장
value = []  # 계산 결과값 저장

def dfs(i, temp, add, sub, mul, div):
    if i == n:
        value.append(temp)
        return

    else:
        if add:
            dfs(i + 1, temp + nlist[i], add - 1, sub, mul, div)
        if sub:
            dfs(i + 1, temp - nlist[i], add, sub - 1, mul, div)
        if mul:
            dfs(i + 1, temp * nlist[i], add, sub, mul - 1, div)
        if div:
            dfs(i + 1, int(temp / nlist[i]), add, sub, mul, div - 1)


dfs(1, nlist[0], add, sub, mul, div)
print(max(value), min(value), sep='\n')