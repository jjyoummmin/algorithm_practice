# == ver 1 - functional ==

import sys
from functools import reduce
lines = sys.stdin.readlines()

def f(set, el):
    set.add(int(el)%42)
    return set

result_set = reduce(f, lines, set())

print(len(result_set))



# == ver 2 ==
s = set()
for i in range(10):
    s.add(int(input())%42)

print(len(s))