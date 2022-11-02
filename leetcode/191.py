# 비트 연산
# n > 0인 동안 rightmost bit이 1인지 확인하고 왼쪽으로 한칸씩 시프트 연산/
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n = n >> 1
        
        return res


# 왼쪽 1부터 성큼성큼 0으로 만들어가는 방법..
# 일단 n > 0 이니까 1개수를 한개 더하고 시작
# 가장 왼쪽 1의 왼쪽은 모두 0인 상황이 계속됨 xxxx100000...000
# xxxx100000...000 & xxxx01111111111 => xxx000000000
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n = n & (n-1)
            
        return res