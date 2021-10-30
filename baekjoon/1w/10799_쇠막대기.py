p = input()
stack, sticknum = [], 0

for i in range(len(p)):
    if p[i] == '(':
        stack.append('(')
    else:
        if len(stack) == 1 and p[i-1] == '(':
            del stack[-1]
        else:
            del stack[-1]
            if p[i-1] == ')':
                sticknum += 1
            else:
                sticknum += len(stack)

print(sticknum)