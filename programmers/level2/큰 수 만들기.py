# number, k = "1924", 2
number, k = "19243241", 4
# number, k = "1231234", 3
# number, k = "4144252841", 4
# number, k = "41424512841", 3
# number, k = "37163964518", 4


def solution(number, k):
    answer = []

    for i, val in enumerate(number):
        if k == 0:  # 빼야할 개수인 k가 0이 됐다면 number에 남은 나머지 값을 answer에 넣어준다.
            answer += number[i:]
            break
        while k > 0 and len(answer) > 0 and answer[-1] < val:   #answer[-1]보다 val이 큰지 비교
            answer.pop()
            k -= 1
        answer.append(val)
    if k > 0:   # k가 0보다 큰 경우
        answer = answer[:-k]
    return ''.join(answer)

print(solution(number, k))



#
# # 그리디 연습 코드
# def greedy(money):
#     m = [500, 100, 50, 10]
#     cnt = 0
#     for i in m:
#         temp = divmod(money, i)
#         print(f'{i}원짜리 동전 : {temp[0]}개')
#         cnt += temp[0]
#         money = temp[1]
#     return cnt
#
# print(f'최소한으로 거슬러주는 동전의 개수 : {greedy(3820)}개')