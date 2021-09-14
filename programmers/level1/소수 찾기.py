n = 10
# n = 5

def solution(n):
    arr = [True] * (n+1)

    for i in range(2, int(n**0.5)+1):
        for j in range(2*i, n+1, i):
            arr[j] = False
    return arr.count(True)-2
# -2는 arr[0],arr[1]을 빼주기 위해서

print(solution(n))