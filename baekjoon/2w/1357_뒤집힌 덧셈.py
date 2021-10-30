a, b = input().split()
print(int(''.join(reversed(str(int(''.join(reversed(a))) + int(''.join(reversed(b))))))))