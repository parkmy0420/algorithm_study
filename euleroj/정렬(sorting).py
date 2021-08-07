n = int(input())
nlist = input().split()
nlist = list(map(int, nlist))

for i in nlist:
    print(i, end = ' ')
nlist = sorted(nlist)
print('')
for i in nlist:
    print(i, end = ' ')
