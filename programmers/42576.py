# ======================= 
# [ HASH ] 완주하지 못한 선수 
# ======================= 

# 처음 풀이 : 각 array sort 후 앞에서부터 한개씩 비교
def solution(participant, completion):
    answer = None
    
    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p == c: 
            continue
        answer = p
        break
        
    answer = answer or participant[-1]
    return answer


# 다른 사람 풀이 : collection 모듈 Counter 데이터 타입 활용
from collections import Counter

def solution(participant, completion):
    subtract = Counter(participant) - Counter(completion)
    return list(subtract)[0]
    