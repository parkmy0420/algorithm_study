a = 5
b = 24

def solution(month, date):
    import datetime
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    return days[datetime.date(2016, month, date).weekday()]

print(solution(a,b))

''' import 사용하지 않고 구현하는 코드

def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

'''