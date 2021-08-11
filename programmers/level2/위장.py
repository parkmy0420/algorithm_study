# clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

def solution(clothes):
    list_clothes, sort_clothes, line_check, answer = [], [], 1, 1

    for i in clothes:
        if i[1] in sort_clothes:
            list_clothes[sort_clothes.index(i[1])] += 1
        else:
            sort_clothes.append(i[1])
            list_clothes.append(line_check)

    for j in list_clothes:
        answer *= j+1

    return answer-1

print(solution(clothes))
