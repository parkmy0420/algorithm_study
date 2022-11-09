from datetime import datetime
def solution(fees, records):
    starttime, startcost, rtime, rcost = fees   # 기본시간, 기본요금, 단위시간, 단위요금
    intime_list, car_in_num, answer = [], [], []  # 입차시간, 입차차번호, 요금계산 후
    car_num_dict = dict()   # 차량 별 주차되어있던 시간

    def inout_time_cul(outtime, car_num):      # 출차시간 - 입차 시간 계산해서 딕셔너리에 저장
        idx = car_in_num.index(car_num)
        del car_in_num[idx]
        intime = intime_list.pop(idx)
        time1 = datetime.strptime(intime, '%H:%M')
        time2 = datetime.strptime(outtime, '%H:%M')
        lap_time = (time2 - time1).seconds // 60
        car_num_dict[car_num] += lap_time

    def cost_cul():
        a, b = divmod((max(0,car_num_dict[now] - starttime)),rtime)
        if b > 0:
            a += 1
        return startcost + a * rcost


    for tmp in records:
        outtime, car_num, inout = tmp.split()
        if inout == 'IN':
            intime_list.append(outtime)
            car_in_num.append(car_num)
            if car_num not in car_num_dict:
                car_num_dict[car_num] = 0
        else:
            inout_time_cul(outtime, car_num)

    while car_in_num:   # 출차하지 않은 차들
        inout_time_cul('23:59', car_in_num[0])

    car_list = sorted(list(car_num_dict.keys()))

    for now in car_list:
        answer.append(cost_cul())

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])) #	[14600, 34400, 5000]
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])) #	[0, 591]
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))     #[14841]