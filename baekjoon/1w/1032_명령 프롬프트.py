num = int(input())
dir = [[*map(str, input())] for _ in range(num)]
for i in range(1, num):
    for j in range(len(dir[0])):
        if dir[0][j] != dir[i][j]:
            dir[0][j] = '?'

print(''.join(dir[0]))

