# arr = [1,1,3,3,0,1,1]
arr = [4,4,4,3,3]

def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
        # else:
        #     continue
    return answer

print(solution(arr))