n = 4
# n = 3
# n = 5
# n = 6

import itertools
def solution(n):
    # 이차원 리스트 초기화 하기
    temp = [[0 for _ in range(0, i)] for i in range(1, n+1)]
    x, y, num = -1, 0, 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            temp[x][y] = num
            num += 1

    return list(itertools.chain.from_iterable(temp))



print(solution(n))