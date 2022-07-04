# =================== 
# [ HASH ] 전화번호 목록 
# =================== 

# 처음 풀이 : 맨 앞자리 숫자로 그룹핑한 뒤 element 개수 >=2 인 것에 대해 재귀..
# 나름 불필요한 boolean 계산 안하게 하려고 generator도 적용했는데, 효율성이 아주아주 꽝이다.

# 테스트 1 〉	통과 (1.91ms, 11.3MB)
# 테스트 2 〉	통과 (1.88ms, 11.3MB)
# 테스트 3 〉	통과 (798.43ms, 254MB)
# 테스트 4 〉	통과 (294.65ms, 41.5MB)

from functools import reduce
from collections import defaultdict


# for lazy evaluation..
def result_generator(arrays):
    for arr in arrays:
        if len(arr) < 2:
            yield True
        elif "" in arr:
            yield False
        else:
            yield rec(arr)


def rec(numbers):
    # group by most significant digit
    msd_dict = defaultdict(list)
    
    for number in numbers:
        first, rest = number[0], number[1:]
        msd_dict[first].append(rest)

    answer = reduce(lambda x,y : x and y, result_generator(msd_dict.values()))
    return answer


def solution(phone_book):
    return rec(phone_book)


# 다른 사람 풀이 : 


# ========================
# [ 참고 ] defaultdict 클래스
# ========================


# ===============
# [ 참고 ] 제너레이터
# ===============