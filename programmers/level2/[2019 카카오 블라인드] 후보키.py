relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
# relation = [['a','aa'],['aa','a'],['a','a']]


from itertools import combinations
def duplicate_check(check_list):    # 중복 체크
    return len(check_list) == len(set(check_list))

def check_uniqueness(relation,cb_check):    # 유일성 체크
    if len(cb_check) == 1:
        return duplicate_check(relation[cb_check[0]])
    else:
        check_temp = []
        for i in range(len(relation[0])):
            temp = []
            for j in cb_check:
                temp.append(relation[j][i])
            check_temp.append(tuple(temp))
        return duplicate_check(check_temp)

def check_minimal(candidates, now_check):   # 최소성 체크
    for i in candidates:
        if set(i).issubset(set(now_check)):
            return False
    return True


def solution(relation):
    relation = list(map(list, zip(*relation)))  # 행렬변환
    cb_len = [i for i in range(len(relation))]  # 속성의 개수만큼 초기화
    candidates = []   # 후보키 후보 리스트

    for i in range(1, len(cb_len)+1):   # 속성의 조합을 인덱스 번호로 구하기
        for cb_check in combinations(cb_len, i):
            if check_minimal(candidates, cb_check) == True:
                check = check_uniqueness(relation, cb_check)
                if check == True:
                    candidates.append(list(cb_check))

    return len(candidates)

print(solution(relation))

