# binary search

class Solution:
    def search(self, nums, target: int) -> int:
        def bsearch(start, end):
            if start > end:
                return -1
            
            mid = start + (end - start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return bsearch(start, mid-1)
            else:
                return bsearch(mid+1, end)
        
        return bsearch(0, len(nums)-1)