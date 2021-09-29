
day = input()
carnum = input().split()
sum = 0

for i in carnum:
    if day == i:
        sum += 1

print(sum)