from sys import stdin
num = int(stdin.readline())
conlist, answer = [[0] for _ in range(num)], 1

for i in range(num):
    conlist[i] = list(map(int, stdin.readline().split()))
conlist.sort()
price = conlist[0][1]

for j in range(1, num):
    if conlist[j][1] < price:
        answer += 1
        price = conlist[j][1]
print(answer)

# 시간 초과가 나오진 않았지만 시간이 많이 걸린 코드
# from sys import stdin
# num = int(stdin.readline())
# conlist = [[0] for _ in range(num)]
# answer = 0
#
# for i in range(num):
#     conlist[i] = list(map(int, stdin.readline().split()))
#
# conlist.sort()
# for x in range(num):
#     answer += 1
#     for check in range(x):
#         if conlist[x][1] >= conlist[check][1]:
#             answer -= 1
#             break
# print(answer)


# c에서는 시간초과 뜨지 않는데 파이썬에서는 시간초과 나옴
# for x in range(num):
#     tfcheck = True
#     for check in range(num):
#         if x != check:
#             if conlist[x][0] >= conlist[check][0] and conlist[x][1] >= conlist[check][1]:
#                 tfcheck = False
#                 break
#     if tfcheck:
#         answer += 1

# for x in range(num):
#     tfcheck = 0
#     for check in range(num):
#         if x != check:
#             if conlist[x][0] > conlist[check][0] and conlist[x][1] >= conlist[check][1]:
#                 tfcheck += 1
#                 break
#             if conlist[x][1] > conlist[check][1] and conlist[x][0] >= conlist[check][0]:
#                 tfcheck += 1
#                 break
#     if tfcheck == 0:
#         answer += 1
