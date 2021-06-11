# absolutes = [4, 7, 12]
# signs = [True, False, True]
absolutes = [1, 2, 3]
signs = [False, False, True]

def solution(absolutes, signs):
    answer = 0

    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else :
            answer -= absolutes[i]
    return answer

print(solution(absolutes,signs))