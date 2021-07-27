# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
# s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s = "{{20,111},{111}}"
# s = "{{123}}"
# s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"

def solution(s):
    from collections import Counter

    temps = [i.replace('{', '').replace('}', '') for i in s.split(',')]
    return [int(temp[0]) for temp in sorted(Counter(temps).items(), key=lambda x: x[1], reverse=True)]

print(solution(s))