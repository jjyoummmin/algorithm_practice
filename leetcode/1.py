class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, x in enumerate(nums):
            compliment = target - x
            if compliment in d:
                return [d[compliment], i]
            d[x] = i