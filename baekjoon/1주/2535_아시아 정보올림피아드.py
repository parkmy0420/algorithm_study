student_num = int(input())
info, point, n_check = [], [], [0]


for i in range(student_num):
    a, b, c = map(int, input().split())
    info.append([a, b])
    point.append(c)
    if len(n_check)-1 != a:
        n_check.append(0)

for _ in range(2):
    s_index = point.index(max(point))
    print(f'{info[s_index][0]} {info[s_index][1]}')
    n_check[info[s_index][0]] += 1
    point[s_index] = 0

s_index = point.index(max(point))
point[s_index] = 0
if n_check[info[s_index][0]] == 2:
    s_index = point.index(max(point))
    print(f'{info[s_index][0]} {info[s_index][1]}')
else:
    print(f'{info[s_index][0]} {info[s_index][1]}')