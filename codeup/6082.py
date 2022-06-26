# 3 6 9 게임

import re

def clap(x):
    return bool(re.search('3|6|9', str(x)))


def result(n):
    arr = [ ('X' if clap(x) else str(x)) for x in range(1, n+1) ]
    result = ' '.join(arr)
    return result

print(result(int(input())))