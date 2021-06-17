# strings = ["sun", "bed", "car"]
# n = 1
strings = ["abce", "cbcd", "cdx", 'aaaa']
n = 2

def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])

print(solution(strings, n))