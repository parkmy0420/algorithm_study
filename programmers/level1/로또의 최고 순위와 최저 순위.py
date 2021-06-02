lottos = [44,1,0,0,31,25]
win_nums = [31,10,45,1,6,19]

#로또 순위 함수
def rank(num):
    if num == 6:
        resultnum = 1
    elif num == 5:
        resultnum = 2
    elif num == 4:
        resultnum = 3
    elif num == 3:
        resultnum = 4
    elif num == 2:
        resultnum = 5
    else :
        resultnum = 6

    return resultnum


#나의 로또와 우승 로또 맞춘 개수 비교 함수(0은 지워져서 알아보기 힘든 숫자)
def solution(lottos, win_nums):

    cp_lottos = list(set(lottos).intersection(win_nums))

    min = rank(len(cp_lottos))
    max = rank(len(cp_lottos) + lottos.count(0))

    answer = [max,min]
    return answer

print(solution(lottos,win_nums))