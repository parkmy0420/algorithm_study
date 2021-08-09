scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
# scores = [[50,90],[50,87]]
# scores = [[70,49,90],[68,50,38],[73,31,100]]

def solution(scores):
    answer = []
    new_scores = list(map(list, zip(*scores)))  # 2차원 리스트 행렬 바꾸기

    for i in range(len(new_scores)):
        if new_scores[i][i] in (min(new_scores[i]), max(new_scores[i])):
            temp = new_scores[i].copy()
            del temp[i]
            if new_scores[i][i] not in temp: # 자기 자신이 유일한 최고점 or 최저점인가?
                del new_scores[i][i]

        avg = sum(new_scores[i])/len(new_scores[i])
        if avg >= 90:
            answer.append('A')
        elif avg >=80:
            answer.append('B')
        elif avg >=70:
            answer.append('C')
        elif avg >=50:
            answer.append('D')
        else:
            answer.append('F')

    return ''.join(answer)

print(solution(scores))