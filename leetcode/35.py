# 선형 탐색
class Solution:
    def searchInsert(self, nums, target):
        for i, x in enumerate(nums):
            if x < target:
                continue
            return i
        return len(nums)


# 이진 탐색
class Solution:
    def searchInsert(self, nums, target):
        def bsearch(start, end):
            if (start == end):
                return start+1 if nums[start] < target else start
            
            mid = start + (end-start)//2
            print(mid)
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                return bsearch(mid+1, end)
            
            return bsearch(start, mid)
        
        return bsearch(0, len(nums)-1)

