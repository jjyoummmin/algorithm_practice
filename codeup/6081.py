# 16진수 구구단

n = int(input(), 16)

for x in range(1, 16):
    y = n*x
    print(f'{n:X}*{x:X}={y:X}')
