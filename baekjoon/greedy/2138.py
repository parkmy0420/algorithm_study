# 2138 전구와 스위치

def two_bulb(one, two):
    before[one] = 1 - before[one]
    before[two] = 1 - before[two]


def three_bulb(one, two, three):
    before[one] = 1 - before[one]
    before[two] = 1 - before[two]
    before[three] = 1 - before[three]


import sys

input = sys.stdin.readline
n = int(input())
before = [0] + list(map(int, input().strip()))
after = [0] + list(map(int, input().strip()))
n1, n2 = before[:], before[:]

if before == after:  # 시작할 때 같은 경우
    print(0)
else:
    for j in range(2):  # j=0: 1번 스위치 누름, j=1: 1번 스위치 누르지 않음
        before = n1 if j == 0 else n2
        cnt = 0

        if j == 0:  # 1번 스위치 누른 경우
            two_bulb(1, 2)
            cnt += 1

        for i in range(2, n + 1):
            if before[i - 1] != after[i - 1]:
                if i <= n - 1:  # 2~(n-1)번 스위치
                    three_bulb(i - 1, i, i + 1)
                    cnt += 1
                elif i == n:  # n번 스위치
                    two_bulb(i - 1, i)
                    cnt += 1

        if before == after:
            print(cnt)
            break

    if before != after:
        print(-1)
