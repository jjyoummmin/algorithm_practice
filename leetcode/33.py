class Solution:
    def search(self, nums, target):
        def bsearch(l, r):
            if l==r:
                return l if nums[l] == target else -1
            mid = l+(r-l)//2
            if nums[mid] == target:
                return mid
            
            # mid in right sorted portion
            if nums[l]<=nums[mid]:
                if nums[l] <= target < nums[mid]:
                    return bsearch(l, mid)
                else:
                    return bsearch(mid+1, r)
            # mid in left sorted portion    
            else:
                if nums[mid] < target <= nums[r]:
                    return bsearch(mid+1, r)
                else:
                    return bsearch(l, mid)
                
        l, r = 0, len(nums)-1
        return bsearch(l, r)