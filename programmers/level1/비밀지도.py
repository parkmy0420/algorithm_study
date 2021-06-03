# n = 5
# arr1 = [9,20,28,18,11]
# arr2 = [30,1,21,17,28]
n = 6
arr1= [46,33,33,22,31,50]
arr2 = [27,56,19,14,14,10]


def solution(n, arr1, arr2):
    answer = [0]*n
    map1 = [[0] * n for _ in range(n)] #map1 0으로 초기화
    map2 = [[0] * n for _ in range(n)]
    resultmap = [[0] * n for _ in range(n)]

    for i in range(n):
        map1[i] = list(format(arr1[i],'b').zfill(n)) #2진수 변환
        map2[i] = list(format(arr2[i],'b').zfill(n)) #2진수 변환

    for j in range(n):
        for k in range(n):
            resultmap[j][k] = int(map1[j][k]) + int(map2[j][k])
            if resultmap[j][k] == 0:
                resultmap[j][k] = ' '
            else :
                resultmap[j][k] = '#'

    for i in range(n):
        answer[i] = ''.join(resultmap[i])

    return answer

print(solution(n,arr1,arr2))


