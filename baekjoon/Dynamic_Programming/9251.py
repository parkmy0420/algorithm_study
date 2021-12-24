# 9251 LCS

a = '0' + input()
b = '0' + input()
lena, lenb = len(a), len(b)
lcs = [[0] * (lenb) for _ in range(lena)]

for i in range(1, lena):
    for j in range(1, lenb):
        if a[i] == b[j]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])

print(lcs[-1][-1])
