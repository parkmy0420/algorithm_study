n, m = 5, 3
#
# def solution(n, m):
#     temp = ''
#     for i in range (m):
#         for j in range (n):
#             temp += '*'
#         print(temp)
#         temp = ''
#
# solution(n, m)

a, b = map(int, input().strip().split(' '))
for i in range (b):
    for j in range (a):
        print('*', end='')
    print()