phone_number = "01033334444"
# phone_number = "027778888"

def solution(phone_number):
    return '*' * (len(phone_number)-4) + ''.join(phone_number[-4:])

print(solution(phone_number))