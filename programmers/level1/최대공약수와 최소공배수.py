# n, m = 3, 12
n, m = 2, 5

def gcd(n, m):
    while (n > 0):
        m,n = n, m % n
    return m

def solution(n,m):
    return [gcd(n, m), int(n*m / gcd(n, m))]

print(solution(n, m))