num = int(input())
if num < 10:
    print(num)
else:
    n = 1
    while len(str(num)) != n:
        if str(num)[-n] == '5':
            num = ((num // int('1'+'0'*n)) + 1) * int('1'+'0'*n)
        else:
            num = round(num, -n)
        n += 1
    print(num)