# Set
from collections import Counter

def solution(s, test_case):
    filtered = [tc for tc in test_case if tc in s]
    print(len(filtered))


if __name__ == '__main__':
    n, m = [int(x) for x in input().split()]
    s = set()
    for _ in range(n):
        s.add(input())
    
    test_case = [input() for _ in range(m)]
    
    solution(s, test_case)