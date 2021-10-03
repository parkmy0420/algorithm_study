#
# day = input()
# carnum = input().split()
# sum = 0
#
# for i in carnum:
#     if day == i:
#         sum += 1
#
# print(sum)

day = int(input())
carnum = list(map(int,input().split()))

print(carnum.count(day))