# 2138

import sys
input = sys.stdin.readline
n = int(input())
scores = [input().split() for _ in range(n)]

for i in range(n):
    p1cnt, p2cnt, setcnt, tf = 0, 0, 0, 0

    for j in range(1, int(scores[i][0])+1):
        if 2 in [p1cnt, p2cnt]:
            tf = 1
            break
        p1, p2 = map(int, scores[i][j].split(':'))

        if p1 >= 6 and p2 >= 6 and j < 3:   # 6:6 count (1,2 set)
            if p1 == 7 and p2 == 6: p1cnt += 1
            elif p1 == 6 and p2 == 7: p2cnt += 1
            else:
                tf = 1
                break
            continue

        if p1 > p2 and (p1 - p2) >= 2 and p1 >= 6: p1cnt += 1
        elif p2 > p1 and (p2 - p1) >= 2 and p2 >= 6: p2cnt += 1
        else:
            tf = 1
            break

    if tf == 0:
        if p1cnt >= 2 or p2cnt >= 2:
            print('Yes')
        else: print('No')
    else:
        print('No')
