num = int(input())
serial = [input().strip() for _ in range(num)]

def sum_serial(x):
    digitsum = 0
    for i in x:
        if i.isdigit():
            digitsum += int(i)
    return digitsum

serial.sort(key=lambda x:(len(x),sum_serial(x), x))

for j in serial:
    print(j)