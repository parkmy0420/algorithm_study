# str1, str2 = 'FRANCE', 'french'
# str1, str2 = 'handshake', 'shake hands'
str1, str2 = 'aa1+aa2', 'AAAA12'
# str1, str2 = 'E=M*C^2', 'e=m*c^2'

def solution(str1, str2):
    str1list, str2list, temp = [], [], []

    for i in range(len(str1)-1):
        temp += [''.join(str1[i:i+2]).lower()]
        if ''.join(temp).isalpha():
                str1list += [temp]
        temp = []

    temp = []
    for i in range(len(str2)-1):
        temp += [''.join(str2[i:i+2]).lower()]
        if ''.join(temp).isalpha():
                str2list += [temp]
        temp = []

    if len(str1list) == 0 | len(str2list) == 0:
        return 65536
    else:
        str1copy, strunion = str1list.copy(), str1list.copy()
        str1copy2, strintersection = str1list.copy(), []

        # 다중집합 합집합
        for j in str2list:
            if j in str1copy:
                del str1copy[str1copy.index(j)]
            else:
                strunion += [j]

        # 다중집합 교집합
        for k in str2list:
            if k in str1copy2:
                strintersection += [k]
                del str1copy2[str1copy2.index(k)]

        return int((len(strintersection) / len(strunion)) * 65536)

print(solution(str1, str2))
