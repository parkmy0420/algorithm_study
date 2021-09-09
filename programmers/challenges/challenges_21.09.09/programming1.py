numbers = [1,2,3,4,6,7,8,0]
# numbers = [5,8,4,0,6,7,9]

# def solution(numbers):
#     check = [0,1,2,3,4,5,6,7,8,9]
#     for i in numbers:
#         del check[check.index(i)]
#
#     return sum(check)

def solution(numbers):
    return sum(set([0,1,2,3,4,5,6,7,8,9]) - set(numbers))

print(solution(numbers))