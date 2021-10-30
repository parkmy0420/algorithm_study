import sys
def find(bingo, findnum):   # idx find def
    for idx1 in range(5):
        if findnum in bingo[idx1]:
            idx2 = (bingo[idx1].index(findnum))
            return idx1, idx2

def linecheck(check): # Bingo check def
    cnt = 0
    for i in check:
        cnt += i.count(5)
        if cnt >= 3: return True
    return False

# main
check, call = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0]], []  # 0:가, 1:세, 2:대
bingo = [[*map(int, input().split())] for _ in range(5)]
for _ in range(5):
    call += list(map(int, sys.stdin.readline().split()))

for i in range(len(call)):
    idx1, idx2 = find(bingo, call[i])
    check[0][idx1] += 1
    check[1][idx2] += 1
    if idx1 + idx2 == 4:
        check[2][0] += 1
    if idx1 == idx2:
        check[2][1] += 1

    if i >= 11 and linecheck(check):
        print(i+1)
        break