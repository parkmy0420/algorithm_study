readlist = []
max = 0

for i in range(5):
    readlist.append(input())
    if max < len(readlist[i]):
        max = len(readlist[i])

for j in range(5):
    if len(readlist[j]) != max:
        for k in range(max - len(readlist[j])):
            readlist[j] += ' '

print(''.join(sum(list(map(list, zip(*readlist))), [])).replace(' ',''))
