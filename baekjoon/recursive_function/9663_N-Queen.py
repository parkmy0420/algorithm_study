# import sys
# input = sys.stdin.readline
# n = int(input())
# board = [0] * n  # 열
# case = 0
#
# def chess(cnt):
#     global case
#     if cnt == n:    # n개 퀸 배치했다면 종료
#         case += 1
#         return
#     for i in range(n):
#         board[cnt] = i
#         if cnt == 0 or check(cnt):
#             chess(cnt+1)
#
#
# def check(cnt):
#     for j in range(cnt):
#         if board[cnt] == board[j] or cnt-j == abs(board[cnt]-board[j]):
#             return False
#     return True
#
# chess(0)
# print(case)

import sys
input = sys.stdin.readline
n = int(input())
case = 0

col_check = [0] * n
d1_check = [0] * n*2
d2_check = [0] * n*2

def chess(cnt):
    global case
    if cnt == n:    # n개 퀸 배치했다면 종료
        case += 1
        return
    for i in range(n):
        if col_check[i] == 0 and d1_check[cnt+i] == 0 and d2_check[cnt-i+n-1] == 0:
            col_check[i] = d1_check[cnt+i] = d2_check[cnt-i+n-1] = 1
            chess(cnt+1)
            col_check[i] = d1_check[cnt+i] = d2_check[cnt-i+n-1] = 0

chess(0)
print(case)