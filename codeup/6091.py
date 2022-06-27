# 여러 수들의 lcm 구하기

from functools import reduce

def gcd(a,b):
    return a if b == 0 else gcd(b, a%b)

def lcm(a,b):
    return int(a*b/gcd(a,b))

arr = [int(x) for x in input().split()]

result = reduce(lambda acc, x: lcm(acc, x), arr)

print(result)