# 124나라
def to_124(n):
    str_124 = lambda x : ['1','2','4'][x]

    subtractor = 0
    divider = 1
    result = ''
    while n >= subtractor:
        digit = (n - subtractor) % ( divider * 3 ) // divider
        result = str_124(digit) + result

        divider *= 3
        subtractor += divider
    return result

def solution(x):
    answer = to_124(x-1)
    return answer
