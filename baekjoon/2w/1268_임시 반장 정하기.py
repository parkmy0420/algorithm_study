s_num = int(input())
students, sameclass = [], []
for _ in range(s_num):
    students.append([*map(int, input().split())])
    sameclass.append([])

for grade in range(5):
    classcheck, check = [[],[],[],[],[],[],[],[],[]], []
    for j in range(s_num):
        ban = students[j][grade] - 1
        classcheck[ban].append(j)
        if len(classcheck[ban]) == 2:
            check.append(ban)
    for k in check:
        for l in classcheck[k]:
            sameclass[l] += classcheck[k]

for cnt in range(s_num):
    sameclass[cnt] = len(set(sameclass[cnt]))
print(sameclass.index(max(sameclass))+1)





# # 시간 초과 코드
# s_num = int(input())
# students, sameclass = [], []
# for _ in range(s_num):
#     students.append([*map(int, input().split())])
#     sameclass.append([])
#
# for i in range(s_num):
#     for grade in range(5):
#         for k in range(i+1, s_num):
#             if k not in sameclass[i] and students[i][grade] == students[k][grade]:
#                 sameclass[i].append(k)
#                 sameclass[k].append(i)
#     sameclass[i] = len(sameclass[i])
#
# print(sameclass.index(max(sameclass))+1)


# 시간 초과 수정 후 정답 코드
# s_num = int(input())
# students, sameclass = [], []
# for _ in range(s_num):
#     students.append([*map(int, input().split())])
#     sameclass.append([])
#
# for i in range(s_num):
#     for k in range(i+1, s_num):
#             for grade in range(5):
#                 if students[i][grade] == students[k][grade]:
#                     sameclass[i].append(k)
#                     sameclass[k].append(i)
#                     break
#     sameclass[i] = len(sameclass[i])
#
# print(sameclass.index(max(sameclass))+1)