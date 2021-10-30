a = input().split()
b = input().split()
awin, bwin = 0, 0

for i in range(10):
    if int(a[i]) > int(b[i]):
        awin += 1
    elif int(b[i]) > int(a[i]):
        bwin += 1

if awin > bwin:
    print('A')
elif bwin > awin:
    print('B')
else:
    print('D')