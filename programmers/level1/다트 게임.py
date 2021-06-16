# dartResult = '1S2D*3T'
# dartResult = '1D2S#10S'
# dartResult = '1D2S0T'
# dartResult = '1S*2T*3S'
# dartResult = '1D#2S*3S'
# dartResult = '1T2D3D#'
dartResult = '1D2S3T*'
# dartResult = ''

def solution(dartResult):
    scoretemp = [0,0,0]
    optiontemp = [1,1,1]
    dartResult = list(dartResult)
    j = 0
    # 점수가 10점인 경우
    for i in range(len(dartResult)):
        if i < len(dartResult) - 1 and dartResult[i] == '1' and dartResult[i+1] == '0':
            dartResult[i] = '10'
            del dartResult[i + 1]

    for i in range(len(dartResult)):
        # 점수 계산
        if dartResult[i].isdigit():
            if dartResult[i+1] == 'S':
                scoretemp[j] = int(dartResult[i]) ** 1
                j += 1
            elif dartResult[i+1] == 'D':
                scoretemp[j] = int(dartResult[i]) ** 2
                j += 1
            elif dartResult[i+1] == 'T':
                scoretemp[j] = int(dartResult[i]) ** 3
                j += 1
        # 옵션 (*, #)인 경우
        elif not dartResult[i].isdigit() and not dartResult[i].isalpha():
            if dartResult[i] == '*':
                if i == 2:
                    optiontemp[j-1] = 2
                elif i > 2:
                    if dartResult[i-3] == '*' or dartResult[i-3] == '#':
                        optiontemp[j-2] *= 2
                        optiontemp[j-1] = 2
                    else:
                        optiontemp[j - 2] = 2
                        optiontemp[j - 1] = 2
            elif dartResult[i] == '#':
                optiontemp[j-1] = -1

    return sum([x*y for x,y in zip(scoretemp,optiontemp)])

print(solution(dartResult))