def solution(survey, choices):
    pointcul = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    point = {'R':0, 'T':1, 'C':2, 'F':3, 'J':4, 'M':5, 'A':6, 'N':7}
    testlist = [0, 0, 0, 0, 0, 0, 0, 0]
    for s, c in zip(survey, choices):
        if c < 4:
            testlist[point[s[0]]] += pointcul[c]
        elif c > 4:
            testlist[point[s[1]]] += pointcul[c]

    convert_point = {v: k for k, v in point.items()}
    answer = ''

    for i in range(0, 8, 2):
        answer += convert_point[i] if testlist[i] >= testlist[i+1] else convert_point[i+1]

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"] ,[7, 1, 3]))