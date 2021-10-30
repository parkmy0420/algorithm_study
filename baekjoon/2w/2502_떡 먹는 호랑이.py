day, ricecakenum = map(int, input().split())
tree, i = [0, day], 1
while i != len(tree):
    now = tree[i]
    if now > 2:
        tree.append(now - 1)
        tree.append(now - 2)
    i += 1
onecnt, twocnt = tree.count(1), tree.count(2)

for j in range(ricecakenum//twocnt, 1, -1):
    minusb = ricecakenum - twocnt * j
    if minusb % onecnt == 0 and int(minusb // onecnt) != 0:
        print(int(minusb // onecnt))
        print(j)
        break
