# for i in input():
#     sum, num = 0, str(ord(i))
#     for j in num:
#         sum += int(j)
#     print(i*sum)


for i in input():
    print(i*sum(map(int, str(ord(i)))))
