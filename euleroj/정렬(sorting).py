n = int(input())
nlist = [int(n) for n in input().split()]

for i in nlist:
    print(i, end = ' ')
nlist = sorted(nlist)
print('')
for i in nlist:
    print(i, end = ' ')
