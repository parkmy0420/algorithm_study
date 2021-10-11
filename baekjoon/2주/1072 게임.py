total, win = map(int, input().split())
percent = win * 100 // total
first, last = 1, total

if percent >= 99:
    print(-1)
else:
    while first <= last:
        mid = (first + last) // 2
        if (win+mid) * 100 // (total+mid) <= percent:
            first = mid + 1
        else:
            answer = mid
            last = mid - 1
    print(answer)



# 풀이 1
# total, win = map(int, input().split())
# percent, time, temp = int(win / total * 100), 0, 0
#
# if total == win:
#     print(-1)
# else:
#     for i in range(1, 1000000000):
#         temp = int((win+i) / (total+i) * 100)
#         time += 1
#         if percent != temp:
#             print(time)
#             break

# 풀이 2
# total, win = map(int, input().split())
# percent = int(win / total * 100)
# first, last = 0, total
#
# if percent >= 99:
#     print(-1)
# else:
#     while True:
#         middle = int(first + last / 2)
#         nowpercent = int((win + middle) / (total + middle) * 100)
#         if percent + 1 == nowpercent:
#             while percent + 1 == int((win + middle) / (total + middle) * 100):
#                 middle -= 1
#             print(middle+1)
#             break
#         elif percent + 1 > nowpercent:
#             first, last = middle, 1000000000
#         else:
#             first, last = 0, middle