# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
# s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
# s = "{{20,111},{111}}"
# s = "{{123}}"
s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"

def solution(s):
    answer, temp, numtemp, digittemp = [], [], [], []

    for i in s:
        if i == '{':
            continue
        if i.isdigit():
            digittemp.append(i)
        else:
            if len(digittemp) != 0:
                numtemp.append(int(''.join(digittemp)))
                digittemp = []
            if i == '}':
                if len(numtemp) != 0:
                    temp += [numtemp]
                    numtemp = []

    temp.sort(key=len)

    for j in range(len(temp)):
        temp[j] = set(temp[j])
        if j == 0:
            answer.append(list(temp[j])[0])
        else:
            answer.append(list(temp[j]-temp[j-1])[0])

    return answer

print(solution(s))