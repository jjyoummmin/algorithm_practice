class Solution:
    def maxSubArray(self, nums):
        maxSum = nums[0]
        curSum = 0
        
        for n in nums:
            # 음수라면 여태까지 더해왔던 값 버리기
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSum = max(maxSum, curSum)
        
        return maxSum