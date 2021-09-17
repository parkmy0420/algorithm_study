# m, musicinfos = "ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# m, musicinfos = "CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
m, musicinfos = "ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]

def sharp_check(melody): # '#'정리 하기
    m_temp = []
    if '#' in melody:
        for k in range(len(melody)):
            if melody[k] == '#':
                m_temp[-1] += '#'
            else:
                m_temp.append(melody[k])
        return m_temp
    else:
        return list(melody)

def solution(m, musicinfos):
    info, play_time, include_m_idx, include_m_time = [], [], [], []
    m = sharp_check(m)  # 기억하는 멜로디 # 정리

    for i in range(len(musicinfos)):
        time = []
        musicinfos[i] = (musicinfos[i].split(','))  # 음악 정보 문자열을 ',' 기준으로 잘라 리스트로 만들기
        # 음악 재생시간 구하기
        time.append(musicinfos[i][0].split(':'))
        time.append(musicinfos[i][1].split(':'))
        play_time.append((int(time[1][0])*60+int(time[1][1])) - (int(time[0][0])*60+int(time[0][1])))
        # info 음악의 # 정리
        m_temp = sharp_check(musicinfos[i][3])

        a, b = divmod(play_time[i], len(m_temp))
        info.append(m_temp * a + m_temp[:b])    # 재생시간만큼의 멜로디
    # 기억하는 멜로디의 음악 제목 찾기
    for j in range(len(info)):
        for l in range(len(info[j])):
            if info[j][l] == m[0]:
                idx = 0
                for check in range(len(m)):
                    if l+idx < len(info[j]) and m[check] == info[j][l+idx]:
                        if check == len(m)-1:
                            include_m_idx.append(j)
                        idx += 1
                    else:
                        break
    if len(include_m_idx) == 1: # 멜로디를 포함하는 음악이 1개
        return musicinfos[include_m_idx[0]][2]
    elif not include_m_idx: # 멜로디를 포함하는 음악이 X
        return '(None)'
    else:   # 멜로디를 포함하는 음악이 여러개
        for i in include_m_idx:
            include_m_time.append(play_time[i])
        return musicinfos[include_m_idx[include_m_time.index(max(include_m_time))]][2]







print(solution(m, musicinfos))