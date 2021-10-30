a, b = map(int, input().split())
c = [input() for _ in range(a)]
answer = 1
for i in range(a-1):
    for j in range(b-1):
        for k in range(min(j+a-1, b-1), j, -1): #
            if c[i][j] == c[i][k]:
                temp = k - j
                if i + temp < a and c[i][j] == c[i+temp][j] == c[i+temp][j+temp]:
                    if answer < (temp + 1) * (temp + 1):
                        answer = (temp+1) * (temp+1)
                    break
print(answer)
