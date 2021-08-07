price, money, count = 5, 20, 4

def solution(price, money, count):
    needmoney = 0

    for i in range(1, count+1):
        needmoney += price * i

    return 0 if money - needmoney >= 0 else needmoney - money

print(solution(price, money, count))