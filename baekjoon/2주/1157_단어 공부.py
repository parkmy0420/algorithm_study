str1 = input().upper()
str2, strcnt = set(str1), []
for i in str2:
    strcnt.append(str1.count(i))

print(list(str2)[strcnt.index(max(strcnt))]) if strcnt.count(max(strcnt)) == 1 else print('?')