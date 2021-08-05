m = int(input())
n =[0]
for i in range(1, m+1):
    if i in(1, 2):
        n.append(1)
    elif i % 2 == 0:
        n.append(n[i//2])
    else:
        n.append(n[(i-1)//2]+n[(i//2)+1])

print(max(n))