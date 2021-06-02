nums = [1,2,7,6,4]

# 소수 구하는 함수
def numsum(sum):
    n = True
    for i in range(2,sum,1):
        if sum % i ==0:
            n = False
            renum = 0
            break
    if n == True:
        renum = 1

    return renum

# 배열에서 3가지 숫자의 합을 구하는 함수
def solution(nums):
    answer = 0
    for i in range(0,len(nums), 1):
        for j in range(i + 1, len(nums), 1):
            for k in range(j + 1, len(nums), 1):
                sum = nums[i] + nums[j] + nums[k]
                answer = answer + numsum(sum)
    return answer


if __name__ == "__main__":
    print(solution(nums))
