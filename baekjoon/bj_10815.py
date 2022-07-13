# Counter 객체 사용해서 풀기
from collections import Counter

def solution(counter, test_case):
    answer = ' '.join([str(counter[tc]) for tc in test_case])
    print(answer)


if __name__ == '__main__':
    input()
    c = Counter([int(x) for x in input().split()])  
    input()
    test_case = [int(x) for x in input().split()]
    
    solution(c, test_case)
