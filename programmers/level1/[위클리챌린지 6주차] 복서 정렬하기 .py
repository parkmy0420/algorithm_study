weights, head2head = [50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]
# weights, head2head = [145,92,86], ["NLW","WNL","LWN"]
# weights, head2head = [60,70,60],  ["NNN","NNN","NNN"]


def solution(weights, head2head):
    answer = []
    for i in range(len(head2head)):
        n = 0
        for j in range(len(head2head[i])):
            if head2head[i][j] == 'W' and weights[i] < weights[j]:  # 무거운 복서를 이긴 횟수
                    n += 1
        # 다른 복서랑 붙어본 적 없는 경우 승률 0
        winning_rate = 0 if len(head2head[i].replace('N','')) == 0 else head2head[i].count('W') / len(head2head[i].replace('N', ''))
        # 0: 승률, 1: 무거운 복서를 이긴 횟수, 2: 자신의 몸무게, 3: 복서 번호
        answer.append([winning_rate, n, weights[i], i+1])
    # 0-3번까지 순서대로 정렬하기 (-x[] : 역순으로 정렬)
    answer = sorted(answer, key=lambda x: (-x[0], -x[1], -x[2], x[3]))
    return [answer[i][3] for i in range(len(answer))]

print(solution(weights,head2head))