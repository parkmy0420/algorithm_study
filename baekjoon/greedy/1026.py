# 1026 보물

import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
b = list(map(int, input().split()))
checkb = list(enumerate(b))
checkb.sort(key=lambda x: (x[1], x[0]))
sorteda = [0]*n

for i in range(n):  # b 크기에 맞게 a 재정렬
    sorteda[checkb[i][0]] = a[i]

s = 0
for j in range(n):  # s 계산
    s += sorteda[j] * b[j]

print(s)