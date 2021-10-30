student_num = int(input())
info, point, n_check, now_n = [], [], [0], 0

for i in range(student_num):
    a, b, c = map(int, input().split())
    info.append([a, b])
    point.append(c)
    if a != now_n:
        n_check.append(0)

while True:
    s_index = point.index(max(point))
    if n_check[info[s_index][0]] != 2:
        print(f'{info[s_index][0]} {info[s_index][1]}')
        if sum(n_check) != 2:
            n_check[info[s_index][0]] += 1
        else:
            break
    point[s_index] = 0

# 금, 은 구하고 동은 따로 구현한 경우
# student_num = int(input())
# info, point, n_check, now_n = [], [], [0], 0
#
# for i in range(student_num):
#     a, b, c = map(int, input().split())
#     info.append([a, b])
#     point.append(c)
#     if a != now_n:
#         n_check.append(0)
#
# for _ in range(2):
#     s_index = point.index(max(point))
#     print(f'{info[s_index][0]} {info[s_index][1]}')
#     n_check[info[s_index][0]] += 1
#     point[s_index] = 0
#
# while tf:
#     s_index = point.index(max(point))
#     point[s_index] = 0
#     if n_check[info[s_index][0]] == 2:
#         tf = True
#     else:
#         print(f'{info[s_index][0]} {info[s_index][1]}')
#         break
