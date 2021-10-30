#v1
# day = input()
# carnum = input().split()
# sum = 0
#
# for i in carnum:
#     if day == i:
#         sum += 1
#
# print(sum)

#v2
day = int(input())
print(list(map(int,input().split())).count(day))

#v3
# day = int(input())
# cnt = 0
# for i in list(map(int,input().split())):
#     if day == i:
#         cnt += 1
# print(cnt)