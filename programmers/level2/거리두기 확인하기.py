# places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],\
#           ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],\
#           ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

places = [["OOPOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"], ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],\
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],\
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OPOPO"]]


def solution(places):
    answer = []
    for i in places:
        checkclass = i
        forbreak = True
        for j in range(5):
            for k in range(5):
                if checkclass[j][k] == 'P':
                    if k < 4: # 맨해튼 1,2인 옆
                        if checkclass[j][k + 1] == 'P':
                            forbreak = False
                            break
                        if k < 3 and checkclass[j][k+2] == 'P':
                            if checkclass[j][k+1] != 'X':
                                forbreak = False
                                break
                    if j < 4: # 맨해튼 1,2인 뒤
                        if checkclass[j+1][k] == 'P':
                            forbreak = False
                            break
                        if j < 3 and checkclass[j+2][k] == 'P':
                            if checkclass[j+1][k] != 'X':
                                forbreak = False
                                break

                    # 맨해튼 = 2 대각선 검사
                    if k != 4 and j != 4: # 맨해튼 = 2 대각선 검사
                        if checkclass[j+1][k+1] == 'P':
                            if checkclass[j][k+1] == 'O' or checkclass[j+1][k] == 'O':
                                forbreak = False
                                break

                    if k != 0 and j != 4:
                        if checkclass[j+1][k-1] == 'P':
                            if checkclass[j][k-1] == 'O' or checkclass[j+1][k] == 'O':
                                forbreak = False
                                break
            if forbreak == False:
                break
        if forbreak == True:
            answer.append(1)
        else:
            answer.append(0)
    return answer

print(solution(places))