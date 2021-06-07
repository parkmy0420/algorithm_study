answers = [2,1,2,3,2,4]

def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    answer = []
    count= [0]*3

    # 맞은 개수 체크 for 문
    for i in range(len(answers)):
        if answers[i] == p1[i % len(p1)]:
            count[0] += 1
        if answers[i] == p2[i % len(p2)]:
            count[1] += 1
        if answers[i] == p3[i % len(p3)]:
            count[2] += 1

    # 가장 많이 맞은 사람 구하는 for 문
    for i in range(3):
        if count[i] == max(count):
            answer.append(i+1)

    return answer

print(solution(answers))