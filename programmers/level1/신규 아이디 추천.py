# new_id = "...!@ BaT#*..y.abcdefg.hijklm "
# new_id = "z-+.^.a"
# new_id = "=.="
# new_id = "123_.def"
# new_id = "abcdefghijklmn.p"
new_id = "......a......a......a....."


def solution(new_id):
    # 1단계 : 대문자를 모두 소문자로 만들기
    id_check = list(new_id.lower())
    result_id = []

    # 2단계 : 소문자, 숫자, '.','_','-' 아닌 경우 제외하기
    for i in range(len(id_check)):
        if not id_check[i].islower() and not id_check[i].isdigit():
            if ord(id_check[i]) in (45, 95, 46, 32):
                result_id.append(id_check[i])
        else:
            result_id.append(id_check[i])

    id_check = result_id
    result_id = []

    if len(id_check) >= 2:
        # 3단계 : '.'이 연속되는 경우 제거하기
        for j in range(len(id_check)):
                if ord(id_check[j]) == 46 and j != len(id_check) -1 and id_check[j] == id_check[j+1]:
                    if j == len(id_check)-1 and id_check[-1] == id_check[-2]: # 마지막 두글자가 '..'인 경우 처리
                        result_id.append(id_check[j])
                        break
                    else:
                        continue
                else:
                    result_id.append(id_check[j])

        id_check = result_id
        result_id = []
    # 4단계 : 처음과 마지막이 '.'인 경우 제거하기
    if len(id_check) >= 1 and ord(id_check[0]) == 46:
        del id_check[0]
    if len(id_check) >= 1 and ord(id_check[-1]) == 46:
        del id_check[-1]

    # 5단계 : 빈칸은 'a'로 대체하기
    id_check = ''.join(id_check).replace(' ','a')
    # 6단계 : 16글자 이상이면 15글자만 남기기
    if len(id_check) >= 16:
        id_check = list(id_check[:15])
    if len(id_check) >= 1 and ord(id_check[-1]) == 46:
        del id_check[-1]
    #7단계 : 3글자 미만인 경우 마지막 글자를 반복시키기
    if len(id_check) <= 2:
        # 아무 글자도 없는 경우에는 'aaa'
        if len(id_check) == 0:
            id_check = 'aaa'
        else:
            result_id = list(id_check)
            while len(result_id) != 3:
                result_id.append(id_check[-1])
            id_check = result_id


    return ''.join(id_check)

print(solution(new_id))