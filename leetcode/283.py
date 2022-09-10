class Solution:
    def moveZeroes(self, nums):
        length = len(nums)
        index = 0
        for _ in range(length):
            if nums[index] != 0:
                index += 1
                continue
            
            nums.pop(index)
            nums.append(0)
        
        return nums