orders, course = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]
# orders, course = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]
# orders, course = ["XYZ", "XWY", "WXA"], [2, 3, 4]

def solution(orders, course):
    from itertools import combinations
    from collections import Counter
    coursetemp, answer = [[]*1 for x in range(len(course))], []

    for i in orders:
        for j in range(len(course)):
            coursetemp[j] += list(combinations(list(i), course[j]))

    for k in range(len(coursetemp)):
        for m in range(len(coursetemp[k])):
            coursetemp[k][m] = tuple(sorted(list(coursetemp[k][m])))
        cnt = Counter(coursetemp[k])
        cntvalues, cntkeys = list(cnt.values()), list(cnt.keys())
        for n in range(len(cntvalues)):
            if cntvalues[n] >= 2 and cntvalues[n] == max(cntvalues):
                answer.append(''.join(cntkeys[n]))

    return sorted(answer)

print(solution(orders,course))