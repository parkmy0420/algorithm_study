nums = [3,3,3,2,2,4]


def solution(nums):
    takeList = set(nums)

    if len(takeList) >= int(len(nums)/2):
        takenums = int(len(nums)/2)
    else:
        takenums = len(takeList)
    return takenums

print(solution(nums))

'''min을 사용하면 훨씬 코드가 간편해짐'''