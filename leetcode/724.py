# find pivot index
# 누적 합 문제

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 누적합 리스트 계산
        sum = 0
        cum_sum = [0]
        for x in nums:
            sum += x
            cum_sum.append(sum)
        
        total_sum = sum
        
        # pivot 찾기
        for i, _ in enumerate(nums):
            left_sum = cum_sum[i]
            right_sum = total_sum - cum_sum[i+1]
            
            if left_sum == right_sum:
                return i
        
        return -1
