from functools import reduce
mult = reduce(lambda acc, x: acc*int(x), [input(), input(), input()], 1)
arr = [int(x) for x in list(str(mult))]

result = [0]*10
for i in arr:
    result[i]+=1

for x in result:
    print(x)