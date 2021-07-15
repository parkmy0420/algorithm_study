arr = [2, 6, 8, 14]
# arr = [1, 2, 3]

def lcm(n,m):
    import math
    return int(n*m / math.gcd(n, m))

def solution(arr):
    numlcm = 1
    for i in range(len(arr)):
        numlcm = lcm(numlcm, arr[i])
    return numlcm

print(solution(arr))