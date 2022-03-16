# 2609 최대공약수와 최소공배수

def gcd(n,m):   # 최대공약수
    while(n>0):
        m,n = n, m % n
    return m

def lcm(n,m):   # 최소공배수
    return int(n*m / gcd(n,m))

n, m = map(int, input().split())
print(gcd(n,m))
print(lcm(n,m))