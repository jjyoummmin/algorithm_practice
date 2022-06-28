# Counter 클래스 사용해서 풀기
from collections import Counter

x = input()
arr = [int(x) for x in input().split()]
dict = dict(Counter(arr))

result_arr = [str(dict.get(x, 0)) for x in range(1,24)]
result = ' '.join(result_arr)
print(result)